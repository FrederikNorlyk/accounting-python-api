from rest_framework import serializers
from accounting.models.expense import Expense
from accounting.models.merchant import Merchant
from accounting.models.project import Project


class ExpenseSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")
    project = serializers.PrimaryKeyRelatedField(many=False, queryset=Project.objects.all())
    merchant = serializers.PrimaryKeyRelatedField(many=False, queryset=Merchant.objects.all())
    project_name = serializers.CharField(source="project.name", read_only=True)
    merchant_name = serializers.CharField(source="merchant.name", read_only=True)

    class Meta:
        model = Expense
        fields = ['id', 'date', 'note', 'amount', 'details', 'project', 'project_name', 'merchant', 'merchant_name', 'user', 'url']