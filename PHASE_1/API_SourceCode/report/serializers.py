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


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = (
            'name',
            'lat',
            'lng',
            'continent',
            'country',
            'state',
            'city'
        )


class ReportEventSerializer(serializers.ModelSerializer):
    report_id = serializers.PrimaryKeyRelatedField(
        queryset=Report.objects.all(), write_only=True)
    location = LocationSerializer()

    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("finish must occur after start")

        # base on fuzz, we send it to the last date it can be or first date it can be to support better filter

        # create location here, use get or create
        return data

    def validate_report_id(self, report_id):
        # wired case, we only want the report id here,
        # but it seems the primarykey related field will seek the
        # object by itself
        return report_id.id

    def validate_location(self, location):
        return Location.objects.get_or_create(location)[0]

    class Meta:
        model = ReportEvent
        fields = (
            "report_id",
            "e_type",
            "start_date",
            "sd_fuzz",
            "end_date",
            "ed_fuzz",
            "number_affected",
            "location"
        )


class SyndromeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Syndrome
        fields = (
            'name',
        )


class DiseaseSerializer(serializers.ModelSerializer):
    syndromes = serializers.PrimaryKeyRelatedField(
        queryset=Syndrome.objects.all(), many=True)

    class Meta:
        model = Disease
        fields = (
            'name',
            'syndromes'
        )


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = (
            'id',
            'url',
            'headline',
            'publish',
            'main_text',
            'p_fuzz',
            'img'
        )


class ReportSerializer(serializers.ModelSerializer):
    # Reportevent details
    report_event = ReportEventSerializer(
        many=True, read_only=True, source='reportevent_set')

    # attach the article while creation
    article = ArticleSerializer(read_only=True)
    # handle these many to many field by using primary key related field
    disease = serializers.PrimaryKeyRelatedField(
        queryset=Disease.objects.all(), many=True
    )
    article_id = serializers.PrimaryKeyRelatedField(
        queryset=Article.objects.all(), write_only=True, source='article')
    syndrome = serializers.PrimaryKeyRelatedField(
        queryset=Syndrome.objects.all(), many=True
    )

    class Meta:
        model = Report
        fields = (
            'id',
            'article',
            'article_id',
            'disease',
            'syndrome',
            'comment',
            'article',
            'report_event'
        )
