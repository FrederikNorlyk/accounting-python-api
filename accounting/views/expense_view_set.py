from rest_framework import viewsets
from rest_framework import permissions
from accounting.permissions.is_owner import IsOwner

from accounting.serializers.expense_serializer import ExpenseSerializer
from accounting.models.expense import Expense


class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


    def get_queryset(self):
        user_id = self.request.user.id
        return Expense.objects.filter(user_id=user_id).order_by("-date")


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    