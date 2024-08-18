from rest_framework import serializers
from .models import BigBox, Offer


class BigBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigBox
        fields = "__all__"


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = "__all__"
