from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Test
from .serializers import TestSerializer
from rest_framework.permissions import IsAuthenticated


class TestList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Test.objects.all()
    serializer_class = TestSerializer
