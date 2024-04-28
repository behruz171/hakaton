from .serializers import *
from django.shortcuts import render
from rest_framework.generics import *
from . import models
from rest_framework import status
from rest_framework.views import Response, APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from django.db.models import Sum
from rest_framework.permissions import IsAuthenticated, AllowAny

class UserAPIView(ListAPIView):
    queryset = models.User.objects.all().filter(type='expert')
    serializer_class = UserListSerializer


class SignleUser(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = SingleUserSerializers


class LogInView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny] 

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)