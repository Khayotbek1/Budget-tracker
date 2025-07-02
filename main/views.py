from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class IncomeListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Income.objects.all()
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['source']
    ordering_fields = ['amount', 'created_at', 'date']

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='ordering',
                in_=openapi.IN_QUERY,
                description='Ordering field by amount, created_at, date',
                type=openapi.TYPE_STRING,
                enum = ['amount', '-amount', 'created_at', '-created_at', '-date', 'date']
            )
        ]
    )
    def get(self, *args, **kwargs):
       return super().get(*args, **kwargs)



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

class ExpenseListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description='Get expense list',
        manual_parameters=[
            openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                description='Search  by source',
                type=openapi.TYPE_STRING
            ),
            openapi.Parameter(
                name='ordering',
                in_=openapi.IN_QUERY,
                description='Ordering by amount, created_at, date',
                type=openapi.TYPE_STRING,
                enum = ['amount', '-amount', 'created_at', '-created_at', '-date', 'date']
            )
        ]
    )

    def get (self, request):
        expense = Expense.objects.filter(user=self.request.user)
        search = request.GET.get('search')
        if search is not None:
            expense = expense.filter(source__icontains=search)

        ordering = request.GET.get('ordering')
        if ordering is not None:
            expense = expense.order_by(ordering)

        serializer = ExpenseSerializer(expense, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ExpenseSerializer
    )
    def post (self, request):
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
