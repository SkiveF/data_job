from rest_framework import serializers
from .models import CovidStats, CovidStatsRegion


class CovidStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidStats
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CovidStatsRegion
        fields = '__all__'
