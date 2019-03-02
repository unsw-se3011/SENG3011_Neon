from .models import Report,Reportevent,Article,Location
from rest_framework import viewsets
from .serializers import ReportSerializer,ReporteventSerializer,LocationSerializer,ArticleSerializer


class ReportViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer

class ReporteventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Reportevent.objects.all()
    serializer_class = ReporteventSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
