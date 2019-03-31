from django.test import TestCase
from .models import ReportEvent, Report, Article
from django.utils.dateparse import parse_datetime
from rest_framework.test import APIRequestFactory, RequestsClient


def parseDatetime(date_time):
    return parse_datetime(date_time)


class ReportEventCase(TestCase):

    def create_report(self):
        article = Article.objects.create(
            url="http://example.com/" + str(self.article_id),
            headline="example",
            publish=parseDatetime("2222-02-02T02:02Z"),
            p_fuzz="D",
            main_text="example text"
        )
        report = Report.objects.create(
            article=article
        )
        self.article_id += 1
        return report

    def setUp(self):
        self.article_id = 0

        report = self.create_report()
        ReportEvent.objects.create(
            report=report, e_type="D",
            start_date=parseDatetime("2222-02-02T02:02Z"),
            sd_fuzz="D",
            end_date=parseDatetime("2222-02-02T02:02Z"),
            number_affected=10
        )

        self.factory = APIRequestFactory()
        self.client = RequestsClient()

    def test_create_reports(self):
        self.assertEqual(Report.objects.count(), 1)

    def test_filter_datetime_simple_include(self):
        # use factory to get the response
        response = self.client.get(
            "http://localhost:8000/v0/reports/?start_date=2222-02-02T02:02:00Z&end_date=2222-03-02T02:02:10Z")
        self.assertEqual(response.json()['count'], 1)

    def test_filter_datetime_simple_not_include(self):
        # use factory to get the response
        response = self.client.get(
            "http://localhost:8000/v0/reports/?start_date=2223-02-02T02:02:00Z&end_date=2223-03-02T02:02:10Z")
        self.assertEqual(response.json()['count'], 0)
