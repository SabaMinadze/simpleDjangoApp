from rest_framework import serializers
from .models import BigBox


class BigBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigBox
        fields = ("id", "firstname", "lastname", "age")