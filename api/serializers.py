from rest_framework import serializers

from api.models import FoodEntry


class FoodEntrySerializer(serializers.ModelSerializer):

    user_name = serializers.CharField(source='user_id.username')

    class Meta:
        model = FoodEntry
        fields = ('id', 'product', 'calories', 'entry_date', 'user_id', 'user_name')