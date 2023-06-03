from rest_framework import viewsets
from rest_framework import permissions
from accounting.permissions.is_owner import IsOwner

from accounting.serializers.project_serializer import ProjectSerializer
from accounting.models.project import Project


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


    def get_queryset(self):
        user_id = self.request.user.id
        return Project.objects.filter(user_id=user_id).order_by("name")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    