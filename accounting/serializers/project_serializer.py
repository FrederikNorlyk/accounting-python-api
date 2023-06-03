from rest_framework import serializers
from accounting.models.project import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source="user.id")

    class Meta:
        model = Project
        fields = ['id', 'name', 'user', 'url']