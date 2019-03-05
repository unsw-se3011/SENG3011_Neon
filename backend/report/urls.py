from django.conf.urls import url, include
from .views import ReportViewSet,\
    ReportEventViewSet,\
    LocationViewSet,\
    ArticleViewSet,\
    UserViewSet
from rest_framework import routers
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token


router = routers.DefaultRouter()
router.register(r'reports', ReportViewSet)
router.register(r'report_events', ReportEventViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'location', LocationViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('jwt/', obtain_jwt_token),

    url(r'^', include(router.urls))
]
