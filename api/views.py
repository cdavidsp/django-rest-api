from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser

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

    def get_queryset(self):
        """
        Check if the user is admin to show all entries
        """
        user = self.request.user
        if user.is_staff:
            return FoodEntry.objects.all()
        else:
            return FoodEntry.objects.filter(assigned_to=user)

    permission_classes = (IsAuthenticated,)
    serializer_class = FoodEntrySerializer
    # pagination_class = ProductsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = FoodEntryFilter


class FoodEntryDetail(generics.RetrieveUpdateDestroyAPIView):

    permission_classes = (IsAuthenticated,)
    serializer_class = FoodEntrySerializer

    def get_queryset(self):
        """
        Check if the user is admin to show all entries
        """
        user = self.request.user
        if user.is_staff:
            return FoodEntry.objects.all()
        else:
            return FoodEntry.objects.filter(assigned_to=user)
