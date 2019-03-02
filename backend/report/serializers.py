from .models import Report,Reportevent,Location,Article,Disease
from rest_framework import serializers,validators
from django.db import models


class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields = ('name','latitude','longitude')
	def create(self,validated_data):
        # Only create a location if it's exist
		return Location.objects.get_or_create(**validated_data)[0]

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = ('url','headline','date_of_publication','main_text')

	def create(self, validated_data):
		validated_data[]

class ReporteventSerializer(serializers.ModelSerializer):
	#location of Reportevent
	location_name = serializers.CharField(source = "Location.name")
	#latitude of Reportevent
	latitude =  serializers.DecimalField(source = "Location.latitude",max_digits=24, decimal_places=20)
	#longitude of Reportevent
	longitude = serializers.DecimalField(source = "Location.longitude",max_digits=24, decimal_places=20)
	#start_date
	start_date = serializers.DateField(source = "Reportevent.start_name")
	#end_date
	end_date = serializers.DateField(source = "Reportevent.end_name")

	def validate(self, data):
		if data['start_date'] > data['end_date']:
			raise serializers.ValidationError("finish must occur after start")
		return data

	class Meta:
		model = Reportevent
		fields = ('report_type','start_date','end_date','number_effecet','location_name','latitude','longitude')

	def update(self, instance, validated_data):
		#pop the foreign
		report_data = validated_data.pop("report",{})
		location = Location.objects.get_or_create(**(profile_data.pop("location")))[0]
		#push back 
		report_data['location'] = location
		#update reportevent
		reportevent = super(ReporteventSerializer, self).update(instance,validated_data)
		reportevent.save()

		LocationSerializer().update(reportevet.location,validated_data=profile_data)
		return reportevent
	
	def create(self,validated_data):
		report_data = validated_data.pop("report",{})
		location = Location.objects.get_or_create(**(profile_data.pop("location")))[0]
		report_data['location'] = location
		reportevent = super(ReporteventSerializer, self).create(validated_data)
		reportevent.save()
		LocationSerializer().update(reportevet.location,validated_data=profile_data)
		return reportevent

class ReportSerializer(serializers.ModelSerializer):
	#Article details
	article =ArticleSerializer()
	#Reportevent details 
	report_event = ReporteventSerializer()
	class Meta:
		model = Report
		fields = ('article','disease','syndrome','report_event','comment')

		