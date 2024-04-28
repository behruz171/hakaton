from django.urls import path
from .views import *
from apps.users.views import *
from apps.users.views import UserAPIView
urlpatterns = [
    path('user-list/', UserAPIView.as_view()),
    path('single-user/<int:pk>', SignleUser.as_view()),
    path('login/', LogInView.as_view()),
]
