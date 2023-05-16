from rest_framework import viewsets
from rest_framework import permissions
from accounting.permissions.is_owner import IsOwner

from accounting.serializers.expense_serializer import ExpenseSerializer
from accounting.models.expense import Expense


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all().order_by("-date");
    serializer_class = ExpenseSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    