from django.urls import path
from .views import *
from apps.users.views import UserAPIView
urlpatterns = [
    path('user-list/', UserAPIView.as_view()),
]
