from .models import Report, ReportEvent, Location, Article, Disease, Syndrome
from rest_framework import serializers, validators
from django.db import models
from django import forms
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "password",
            "first_name",
            "last_name"
        )

    def update(self, instance, validated_data):
        # update the user by given validated data
        user = super(UserSerializer, self)\
            .update(instance, validated_data)
        # update it's password
        user.set_password(validated_data['password'])
        user.save()
        return user

    def create(self, validated_data):
        # create user and udpate it's password
        user = super(UserSerializer, self)\
            .create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'url',
            'headline',
            'publish',
            'main_text',
            'p_fuzz',
        )


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('name', 'lat', 'lng')


class ReportEventSerializer(serializers.ModelSerializer):
    def validate(self, data):
        if start_date > end_date:
            raise serializers.ValidationError("finish must occur after start")
        return data

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


class SyndromeSerializer(serializers.ModelSerializer):
    class Meta:
        models = Syndrome
        fields = (
            'name'
        )


class DiseaseSerializer(serializers.ModelSerializer):
    class Meta:
        models = Disease
        fields = (
            'name',
            'syndromes'
        )


class ReportSerializer(serializers.ModelSerializer):
    # Article details
    article = ArticleSerializer(read_only=True)
    # Reportevent details
    report_event = ReportEventSerializer()

    class Meta:
        model = Report
        fields = (
            'article',
            'disease',
            'syndrome',
            'comment',
            'article',
            'report_event'
        )
