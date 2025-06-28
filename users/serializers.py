from rest_framework.serializers import ModelSerializer
from .models import User

class UserRegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'balance')
        extra_kwargs = {
            'password': {'write_only': True},
            'balance': {'required': False},
        }