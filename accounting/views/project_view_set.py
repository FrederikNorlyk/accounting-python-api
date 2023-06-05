from django.db import IntegrityError
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

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
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            raise ValidationError({'detail': 'A project with that name already exists'})

    
    def perform_update(self, serializer):
        try:
            return super().perform_update(serializer)
        except IntegrityError:
            raise ValidationError({'detail': 'A project with that name already exists'})
