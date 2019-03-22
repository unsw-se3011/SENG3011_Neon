from rest_framework.filters import BaseFilterBackend, SearchFilter
from django.db.models import Q
from rest_framework.compat import coreapi, coreschema
from datetime import datetime
from django.utils.dateparse import parse_datetime


class DatetimeFilter(BaseFilterBackend):
    def get_search_fields(self, view, request):
        return getattr(view, 'time_field', None)

    def filter_queryset(self, request, queryset, view):
        search_filed = self.get_search_fields(view, request)

        if not search_filed:
            return queryset

        start_date = datetime.strptime(
            request.query_params.get(
                "start_date", None), '%Y-%m-%dT%H:%M:%S'
        )
        end_date = datetime.strptime(
            request.query_params.get("end_date", None), '%Y-%m-%dT%H:%M:%S'
        )

        if not start_date or not end_date:
            return queryset
        queryset.filter(
            Q(**{search_filed + "__gte": start_date}) &
            Q(**{search_filed + "__lte": end_date}))
        return queryset

    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name="start_date",
                required=False,
                location='query',
                schema=coreschema.String(
                    title="start date",
                    description="Start datetime for filetring"
                )
            ),
            coreapi.Field(
                name="end_date",
                required=False,
                location='query',
                schema=coreschema.String(
                    title="end date",
                    description="End datetime for filetring"
                )
            ),
        ]


class ReportEventDatetimeRangeFilter(BaseFilterBackend):
    """
    This could only be use at report class
    """

    def filter_queryset(self, request, queryset, view):

        try:
            start_date = parse_datetime(
                request.query_params.get(
                    "start_date", None
                )
            )
            end_date = parse_datetime(
                request.query_params.get("end_date", None)
            )
        except Exception as e:
            return queryset

        return queryset.filter(
            Q(
                reportevent__start_date__gte=start_date,
                reportevent__start_date__lte=end_date
            ) |
            Q(
                reportevent__end_date__gte=start_date,
                reportevent__end_date__lte=end_date
            ) |
            Q(
                reportevent__start_date__lte=start_date,
                reportevent__end_date__gte=end_date
            )
        )

    def get_schema_fields(self, view):
        return [
            coreapi.Field(
                name="start_date",
                required=False,
                location='query',
                schema=coreschema.String(
                    title="start date",
                    description="Start datetime of the event occour"
                )
            ),
            coreapi.Field(
                name="end_date",
                required=False,
                location='query',
                schema=coreschema.String(
                    title="end date",
                    description="End datetime of the event occour "
                )
            ),
        ]


class KeytermFilter(SearchFilter):
    search_param = "key_term"
