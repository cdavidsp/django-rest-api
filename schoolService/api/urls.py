# api/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = [
    path('tests', views.TestList.as_view()),
    path('tests/<int:pk>', views.TestDetail.as_view()),
]