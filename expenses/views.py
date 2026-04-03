from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend

from .models import Category, Expense
from .serializers import CategorySerializer, ExpenseSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    class Meta:
        model = Category
        fields = ['id', 'name'] # 'user' is omitted here so it doesn't show up in the form

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        # This tells Django: "Take the logged-in user and save it as the owner"
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Instead of .all(), only return items belonging to the person logged in
        return Category.objects.filter(user=self.request.user)


class TotalSpentPagination(PageNumberPagination):
    def get_paginated_response(self, data):
        # We get the filtered queryset from the view directly
        # instead of trying to access it through the User object
        view = self.request.parser_context['view']
        queryset = view.filter_queryset(view.get_queryset())
        total = queryset.aggregate(Sum('amount'))['amount__sum'] or 0

        return Response({
            'total_spent': total,
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    pagination_class = TotalSpentPagination # Add this line

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title'] # Allows you to search by title
    filterset_fields = ['category', 'date'] # Adds exact date filtering
    ordering_fields = ['amount', 'date'] # Allows you to sort by price or date

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        # Instead of .all(), only return items belonging to the person logged in
        return Expense.objects.filter(user=self.request.user)

    # This is a custom endpoint that calculates the total expenses for the logged-in user
    @action(detail=False, methods=['get'])
    def summary(self, request):
        # Calculate total for the logged-in user
        total = self.get_queryset().aggregate(Sum('amount'))['amount__sum'] or 0
        return Response({'total_expense': total})
