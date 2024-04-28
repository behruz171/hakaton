from rest_framework import serializers
from .models import *


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'img', 'type', 'description', 'category']