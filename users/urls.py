from django.urls import path
from rest_framework_simplejwt.views import token_obtain_pair, token_refresh
from .views import *

urlpatterns = [
    path('token/', token_obtain_pair, name='token'),
    path('token/refresh/', token_refresh, name='token-refresh'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('profile/', ProfileAPIView.as_view(), name='profile'),
]