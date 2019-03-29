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
# swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
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

# swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('jwt/', obtain_jwt_token),
    url(r'^jwt_refresh/', refresh_jwt_token),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),
    url(r'^', include(router.urls))
]
