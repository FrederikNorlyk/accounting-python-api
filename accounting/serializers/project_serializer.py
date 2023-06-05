from django.db.models import Sum

from rest_framework import serializers
from accounting.models.project import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")
    total_amount = serializers.SerializerMethodField()


    class Meta:
        model = Project
        fields = ['id', 'name', 'user', 'total_amount', 'url']

    def get_total_amount(self, obj):
        return obj.expenses.aggregate(Sum('amount'))['amount__sum']