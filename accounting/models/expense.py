from django.db import models
from accounting.models.merchant import Merchant
from accounting.models.project import Project


class Expense(models.Model):
    _related_name = "expenses"

    date = models.DateTimeField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    note = models.TextField()
    details = models.TextField(null=True)
    project = models.ForeignKey(Project, related_name=_related_name, on_delete=models.SET_NULL, null=True)
    merchant = models.ForeignKey(Merchant, related_name=_related_name, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey("auth.User", related_name=_related_name, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return f'{self.date} - {self.note} - {self.amount} - p:{self.project} - m:{self.merchant} - u:{self.user}'
