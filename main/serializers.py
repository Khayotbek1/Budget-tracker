from rest_framework.serializers import ModelSerializer
from .models import *
from users.serializers import ProfileSerializer

class IncomeCreateSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = ('id', 'amount', 'source', 'date', 'created_at')

class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'


class IncomeSafeSerializer(ModelSerializer):
    user = ProfileSerializer(read_only=True)
    class Meta:
        model = Income
        fields = '__all__'