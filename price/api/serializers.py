from rest_framework import serializers

from price.models import Price


class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = ("price", "created_at")
