from . import serializers
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from . import models
from rest_framework.views import Response, APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserAPIView(ListAPIView):
    queryset = models.User.objects.all().filter(type='expert')
    serializer_class = serializers.UserListSerializer