from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from .models import FoodEntry
from .serializers import FoodEntrySerializer

from django_filters import rest_framework as filters, DateFilter


class FoodEntryFilter(filters.FilterSet):
    start_date = DateFilter(field_name='created_date', lookup_expr=('gt'), )
    end_date = DateFilter(field_name='created_date', lookup_expr=('lt'))

    class Meta:
        model = FoodEntry
        fields = []


class FoodEntryListView(generics.ListCreateAPIView):
    """List of all entries """

    queryset = FoodEntry.objects.all()
    serializer_class = FoodEntrySerializer
    # pagination_class = ProductsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = FoodEntryFilter


class FoodEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodEntry.objects.all()
    serializer_class = FoodEntrySerializer