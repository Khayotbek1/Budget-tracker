from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import *


class IncomeListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = IncomeCreateSerializer
    queryset = Income.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)