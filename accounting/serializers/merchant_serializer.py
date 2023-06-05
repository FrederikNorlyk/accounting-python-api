from rest_framework import serializers
from django.db.models import Sum, Count

from accounting.models.merchant import Merchant


class MerchantSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")
    total_amount = serializers.SerializerMethodField()
    number_of_expenses = serializers.SerializerMethodField()

    class Meta:
        model = Merchant
        fields = ['id', 'name', 'user', 'total_amount', 'number_of_expenses', 'url']

    def get_total_amount(self, obj):
        return obj.expenses.aggregate(Sum('amount'))['amount__sum']
    
    def get_number_of_expenses(self, obj):
        return obj.expenses.aggregate(Count('id'))['id__count']