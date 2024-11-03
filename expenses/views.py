from rest_framework import viewsets
from .models import User, Expense
from .serializers import UserSerializer, ExpenseSerializer

import csv
from django.db.models import Sum
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Expense
from .serializers import UserSerializer, ExpenseSerializer


# User ViewSet
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Expense ViewSet
class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

    def create(self, request, *args, **kwargs):
        """
        Endpoint to create an expense.
        """
        participants = request.data.get('participants', [])

        if not participants:
            return Response(
                {"detail": "Participants list cannot be empty."},
                status=status.HTTP_400_BAD_REQUEST
            )

        return super().create(request, *args, **kwargs)

    @action(detail=False, methods=['get'])
    def overall_expenses(self, request):
        """
        Endpoint to retrieve total expenses for each user.
        """
        overall_expenses = (
            Expense.objects.values('user__name')
            .annotate(total_amount=Sum('amount'))
            .order_by('-total_amount')
        )
        return Response(overall_expenses)

    @action(detail=False, methods=['get'])
    def download_balance_sheet(self, request):
        """
        Endpoint to download a CSV balance sheet with total expenses per user.
        """
        # Create CSV response
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="balance_sheet.csv"'

        writer = csv.writer(response)
        writer.writerow(['User', 'Total Expenses'])

        # Aggregate and write each user's total expenses
        overall_expenses = (
            Expense.objects.values('user__name')
            .annotate(total_amount=Sum('amount'))
            .order_by('-total_amount')
        )
        for expense in overall_expenses:
            writer.writerow([expense['user__name'], expense['total_amount']])

        return response

