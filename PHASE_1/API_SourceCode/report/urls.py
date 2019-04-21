from django.conf.urls import url, include
from .views import (
    ReportViewSet,
    ReportEventViewSet,
    LocationViewSet,
    ArticleViewSet,
    UserViewSet,
    DiseaseViewSet,
    SyndromeViewSet,
    OutbreakViewSet,
    MessageViewSet
)
from rest_framework import routers
# from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# register viewset
router = routers.DefaultRouter()
router.register(r'reports', ReportViewSet)
router.register(r'report_events', ReportEventViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'location', LocationViewSet)
router.register(r'users', UserViewSet)
router.register(r'diseases', DiseaseViewSet)
router.register(r'syndromes', SyndromeViewSet)
router.register(r'outbreaks', OutbreakViewSet)
router.register(r'message', MessageViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^jwt/$', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^jwt_refresh/$', TokenRefreshView.as_view(), name='token_refresh'),
]
