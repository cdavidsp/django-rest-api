from rest_framework import serializers

from api.models import FoodEntry


class FoodEntrySerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(source='assigned_to.username')

    class Meta:
        model = FoodEntry
        fields = ('id', 'product', 'calories', 'created_date', 'assigned_to', 'user_name')