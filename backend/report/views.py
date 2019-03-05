from .serializers import *
from rest_framework import viewsets
from .serializers import ReportSerializer, ReportEventSerializer, LocationSerializer, ArticleSerializer
from rest_framework.exceptions import NotAuthenticated
from rest_framework.permissions import AllowAny, IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

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


class ReportEventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ReportEvent.objects.all()
    serializer_class = ReportEventSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
