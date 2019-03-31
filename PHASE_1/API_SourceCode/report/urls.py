from django.conf.urls import url, include
from .views import ReportViewSet,\
    ReportEventViewSet,\
    LocationViewSet,\
    ArticleViewSet,\
    UserViewSet,\
    DiseaseViewSet,\
    SyndromeViewSet
from rest_framework import routers
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework import permissions

# register viewset
router = routers.DefaultRouter()
router.register(r'reports', ReportViewSet)
router.register(r'report_events', ReportEventViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'location', LocationViewSet)
router.register(r'users', UserViewSet)
router.register(r'diseases', DiseaseViewSet)
router.register(r'syndromes', SyndromeViewSet)

urlpatterns = [
    path('jwt/', obtain_jwt_token),
    url(r'^jwt_refresh/', refresh_jwt_token),
    url(r'^', include(router.urls))
]
