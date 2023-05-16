from rest_framework import serializers
from accounting.models.expense import Expense
from accounting.models.merchant import Merchant
from accounting.models.project import Project


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")
    project = serializers.PrimaryKeyRelatedField(many=False, queryset=Project.objects.all())
    merchant = serializers.PrimaryKeyRelatedField(many=False, queryset=Merchant.objects.all())

    class Meta:
        model = Expense
        fields = ['id', 'date', 'note', 'amount', 'details', 'project', 'merchant', 'user', 'url']