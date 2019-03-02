from .models import Report,Reportevent,Location,Article
from rest_framework import serializers

class ReportSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Report
		fields = ('article','disease','syndrome','comment')

class ReporteventSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Reportevent
		fields = ('report_type','start_date','end_date','number_effecet','location')

class LocationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Location
		fields = ('name','latitude','longitude')

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Article
		fields = ('url','headline','date_of_publication','main_text')