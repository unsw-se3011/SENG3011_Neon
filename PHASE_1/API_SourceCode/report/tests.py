from django.test import TestCase
from .models import ReportEvent, Report, Article


class ReportEventCase(TestCase):

    def create_report(self):
        article = Article.objects.create(
            "http://example.com/" + str(self.article_id),
            "example",
            "2222-02-02T02:02",
            "D",
            "example text"
        )
        report = Report.objects.create(
            article
        )
        self.article_id += 1
        return report

    def setUp(self):
        self.article_id = 0

        report = self.create_report()
        ReportEvent.objects.create(
            report, "D", "2222-02-02T02:02",
            "D", "2222-02-02T02:02", 10
        )

    def test_create_reports(self):
        self.assertEqual(Report.objects.count(), 1)
