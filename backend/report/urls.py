from django.conf.urls import url, include
from .views import ReportViewSet, ReportEventViewSet, LocationViewSet, ArticleViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'reports', views.ReportViewSet)
router.register(r'report_events', views.ReportEventViewSet)
router.register(r'articles', views.ArticleViewSet)
router.register(r'location', views.LocationViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
