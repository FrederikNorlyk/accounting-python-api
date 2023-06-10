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
        sort_field = self.request.query_params.get('sortField', "name")
        sort_dir: str = self.request.query_params.get('sortDir', "")

        sort = sort_dir = "" if sort_dir == "ASC" else "-"
        sort += sort_field

        return Project.objects.filter(user_id=user_id).order_by(sort)

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
