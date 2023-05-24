from rest_framework import serializers
from accounting.models.expense import Expense
from accounting.models.project import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = Project
        fields = ['id', 'name', 'user', 'url']