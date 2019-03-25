from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from .serializers import ReportSerializer, ReportEventSerializer, LocationSerializer, ArticleSerializer
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .filter import ReportEventDatetimeRangeFilter, KeytermFilter

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
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (
        ReportEventDatetimeRangeFilter,
        DjangoFilterBackend, KeytermFilter,
    )

    search_fields = (
        'article__headline', 'article__main_text',
        'disease__name', 'syndrome__name',
    )
    filterset_fields = (
        'article__headline',
        'reportevent__location__continent',
        'reportevent__location__country',
        'reportevent__location__state',
        'reportevent__location__city',
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
