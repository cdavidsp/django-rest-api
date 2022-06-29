# api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('food-entries', views.FoodEntryListView.as_view()),
    path('food-entries/<int:pk>', views.FoodEntryDetail.as_view())
]