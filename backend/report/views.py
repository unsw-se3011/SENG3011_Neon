from .serializers import *
from rest_framework import viewsets
from .serializers import ReportSerializer, ReportEventSerializer, LocationSerializer, ArticleSerializer
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


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


class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, ser_er):
        # user report serializer to create this report
        report = ser_er.save()
        try:
            # if len(self.request.data['report_events']) == 0:
            #     raise serializers.ValidationError({
            #         "report_events": "report_events at least have one instance"
            #     })

            for re in self.request.data['report_events']:

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
            raise e
            print(e)
            raise serializers.ValidationError({
                'report_event': 'Error in createing report events'
            })


class ReportEventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ReportEvent.objects.all()
    serializer_class = ReportEventSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (filters.SearchFilter, DjangoFilterBackend,)


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
