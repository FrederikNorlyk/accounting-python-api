from rest_framework import serializers
from django.contrib.auth.models import User

from accounting.models.expense import Expense
from accounting.models.merchant import Merchant
from accounting.models.project import Project


class UserSerializer(serializers.HyperlinkedModelSerializer):
    expenses = serializers.PrimaryKeyRelatedField(many=True, queryset=Expense.objects.all())
    projects = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())
    merchants = serializers.PrimaryKeyRelatedField(many=True, queryset=Merchant.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'expenses', 'projects', 'merchants', 'url']