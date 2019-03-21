from rest_framework.filters import BaseFilterBackend
from django.db.models import Q
from rest_framework.compat import coreapi, coreschema
from datetime import datetime


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
        print("imhere")
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

