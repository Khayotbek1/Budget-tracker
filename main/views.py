from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS

from .serializers import *


class IncomeListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Income.objects.all()

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return IncomeSafeSerializer
        return IncomeCreateSerializer


    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        user.balance += serializer.validated_data['amount']
        user.save()
        serializer.save(user=self.request.user)