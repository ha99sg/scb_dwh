from rest_framework import serializers

from api.base.serializers import InheritedSerializer
from config.settings import DATETIME_INPUT_OUTPUT_FORMAT

class ChartFRequestSerializer(InheritedSerializer):
    name = serializers.CharField(help_text="`name` of chart")
    region = serializers.CharField(help_text="`region` of chart")
    unit = serializers.CharField(help_text="`unit` of chart")

class ChartFResponseSerializer(InheritedSerializer):
    key = serializers.CharField(help_text="`key` of data")
    label = serializers.CharField(help_text="`label` of data")
    val = serializers.IntegerField(help_text="`val` of data")
    unit = serializers.CharField(help_text="`unit` of data")

class DataResponseSerializer(InheritedSerializer):
    id = serializers.CharField(help_text="`id` of data")
    title = serializers.CharField(help_text="`title` of data")
    day = serializers.IntegerField(help_text="`day` of data")
    week = serializers.IntegerField(help_text="`week` of data")
    month = serializers.IntegerField(help_text="`month` of data")
    accumulated = serializers.IntegerField(help_text="`accumulated` of data")
    unit = serializers.CharField(help_text="`unit` of data")
