from django.db.models import Sum, Min, Max

from rest_framework import serializers
from accounting.models.project import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")
    total_amount = serializers.SerializerMethodField()
    from_date = serializers.SerializerMethodField()
    to_date = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ['id', 'name', 'user', 'total_amount', 'from_date', 'to_date', 'url']

    def get_total_amount(self, obj):
        return obj.expenses.aggregate(Sum('amount'))['amount__sum']
    
    def get_from_date(self, obj):
        return obj.expenses.aggregate(Min('date'))['date__min']
    
    def get_to_date(self, obj):
        return obj.expenses.aggregate(Max('date'))['date__max']