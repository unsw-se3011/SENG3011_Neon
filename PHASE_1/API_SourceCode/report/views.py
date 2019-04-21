from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .serializers import ReportSerializer, ReportEventSerializer, LocationSerializer, ArticleSerializer
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
# support custom actions
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .filter import ReportEventDatetimeRangeFilter, KeytermFilter, LocationFilter

import traceback


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    """
    Get method could only get the element of current user
    """

    def list(self, request):
        if request.user and request.user.is_authenticated:
            serializer = UserSerializer(request.user)
            return Response(serializer.data)
        # else: not authenticated
        # raise not authenticated
        raise NotAuthenticated()

    def retrieve(self, request, pk=None):
        return self.list(request)


class ReportEventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ReportEvent.objects.all()
    serializer_class = ReportEventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Report.objects.order_by('-article__date_of_publication')
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (
        ReportEventDatetimeRangeFilter, LocationFilter,
        DjangoFilterBackend, KeytermFilter,
    )

    search_fields = (
        'article__headline',
        'article__main_text',
        'disease__name',
        'syndrome__name',
    )
    filterset_fields = (
        'article__headline',
        'disease',
        'syndrome',
    )
    ordering_fields = ('article__publish',)

    def perform_create(self, ser_er):
        # user report serializer to create this report
        report = ser_er.save()
        try:
            for re in self.request.data.get('report_events', []):
                # filling the missing information
                re['report_id'] = report.id
                # use re serializer to perform this creation
                re_s = ReportEventSerializer(data=re)
                re_s.is_valid(raise_exception=True)
                # we get the instance
                re = re_s.save()
                # wrap the re creation
                report.reportevent_set.add(re)
        except serializers.ValidationError as e:
            raise e
        except Exception as e:
            report.delete()

            raise serializers.ValidationError({
                'report_event': 'Error in createing report events'
            })


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    search_fields = ('headline', 'main_text')
    filterset_fields = (
        'headline',
        'id'
    )
    time_field = 'publish'
    ordering_fields = ('publish',)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class DiseaseViewSet(viewsets.ModelViewSet):
    queryset = Disease.objects.all()
    serializer_class = DiseaseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class SyndromeViewSet(viewsets.ModelViewSet):
    queryset = Syndrome.objects.all()
    serializer_class = SyndromeSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class OutbreakViewSet(viewsets.ModelViewSet):
    queryset = Outbreak.objects.order_by('-end_date')
    serializer_class = OutbreakSerializer

    @action(detail=True, methods=['GET'], name='chart_data')
    def chart(self, request, pk=None):
        query_set = Outbreak.static(pk)
        day_dict = {}
        country_dict = {}
        shown_key = set()
        # show logic
        for re in query_set:
            date_str = re.start_date.strftime("%Y-%m-%d")
            # record all the key shown
            shown_key.add(re.event_type_full)
            if date_str not in day_dict:
                day_dict[date_str] = {
                    re.event_type_full: re.number_affected,
                    'date': date_str
                }
            else:
                day_dict[date_str][re.event_type_full] = \
                    re.number_affected

            if re.location:
                if re.location.country not in country_dict:
                    country_dict[re.location.country] = 0
                country_dict[re.location.country] += re.number_affected

        ret = {
            # calculate only for the shown reusults
            'columns': ['date']+[k for k in shown_key],
            'rows': [day_dict[d] for d in day_dict],
            'map_arr': [["Country", "Affected"]] + [
                [k, country_dict[k]] for k in country_dict
            ]
        }
        # return the filtered result
        return Response(
            ret
        )


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
