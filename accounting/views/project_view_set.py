from rest_framework import viewsets
from rest_framework import permissions
from accounting.permissions.is_owner import IsOwner

from accounting.serializers.project_serializer import ProjectSerializer
from accounting.models.project import Project


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all();
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    