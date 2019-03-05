from .models import Report, ReportEvent, Location, Article, Disease
from rest_framework import serializers, validators
from django.db import models
from django import forms


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'url',
            'headline',
            'date_of_publication',
            'main_text'
        )


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'lat', 'lng')

    # def create(self, validated_data):
    #     # Only create a location if it's exist
    #     return Location.objects.get_or_create(**validated_data)[0]


class ReportEventSerializer(serializers.ModelSerializer):
    # def validate(self, data):
    #     if start_date > end_date:
    #         raise serializers.ValidationError("finish must occur after start")
    #     return data

    # def validate(self,cleaned_data):
    #             start_date = cleaned_data.get("start_date")
    #             end_date = cleaned_data.get("end_date")
    #             if end_date < start_date:
    #                     msg = u"End date should be greater than start date."
    #                     self._errors["end_date"] = self.error_class([msg])
    class Meta:
        model = ReportEvent
        fields = (
            'report_type',
            'start_date',
            'sd_fuzz',
            'end_date',
            'ed_fuzz',
            'number_effecet',
            'location',
            'report'
        )

    # def update(self, instance, validated_data):
    #     # pop the foreign
    #     report_data = validated_data.pop("report", {})
    #     location = Location.objects.get_or_create(
    #         **(profile_data.pop("location")))[0]
    #     # push back
    #     report_data['location'] = location
    #     # update reportevent
    #     reportevent = super(ReportEventSerializer, self).update(
    #         instance, validated_data)
    #     reportevent.save()

    #     LocationSerializer().update(reportevet.location, validated_data=profile_data)
    #     return reportevent

    # def create(self, validated_data):
    #     report_data = validated_data.pop("report", {})
    #     location = Location.objects.get_or_create(
    #         **(profile_data.pop("location")))[0]
    #     report_data['location'] = location
    #     reportevent = super(ReportEventSerializer, self).create(validated_data)
    #     reportevent.save()
    #     LocationSerializer().update(reportevet.location, validated_data=profile_data)
    #     return reportevent


class ReportSerializer(serializers.ModelSerializer):
    # Article details
    article = ArticleSerializer()
    # Reportevent details
    report_event = ReportEventSerializer()

    class Meta:
        model = Report
        fields = (
            'article',
            'disease',
            'syndrome',
            'comment'
        )
