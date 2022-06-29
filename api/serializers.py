from rest_framework import serializers

from api.models import FoodEntry


class FoodEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodEntry
        fields = ('id', 'product', 'calories', 'created_date')