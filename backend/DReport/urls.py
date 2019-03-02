"""DReport URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.views import generic
from rest_framework import routers
from report import views

router = routers.DefaultRouter()
router.register(r'reports', views.ReportViewSet,base_name='report')
router.register(r'reportsevent', views.ReporteventViewSet,base_name='reportevent')
router.register(r'Article', views.ArticleViewSet,base_name='Article')
router.register(r'Location', views.LocationViewSet,base_name='Location')

urlpatterns = [
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
   
]
