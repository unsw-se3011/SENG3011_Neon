from django.conf.urls import url, include
from .views import ReportViewSet,\
    ReportEventViewSet,\
    LocationViewSet,\
    ArticleViewSet,\
    UserViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'reports', ReportViewSet)
router.register(r'report_events', ReportEventViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'location', LocationViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
