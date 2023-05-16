from rest_framework import serializers
from accounting.models.expense import Expense
from accounting.models.merchant import Merchant


class MerchantSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")
    expenses = serializers.PrimaryKeyRelatedField(many=True, queryset=Expense.objects.all())

    class Meta:
        model = Merchant
        fields = ['id', 'name', 'user', 'expenses', 'url']