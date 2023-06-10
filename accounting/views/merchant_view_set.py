from django.db import IntegrityError
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.exceptions import ValidationError

from accounting.permissions.is_owner import IsOwner
from accounting.serializers.merchant_serializer import MerchantSerializer
from accounting.models.merchant import Merchant


class MerchantViewSet(viewsets.ModelViewSet):
    serializer_class = MerchantSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


    def get_queryset(self):
        user_id = self.request.user.id
        sort_field = self.request.query_params.get('sortField', "name")
        sort_dir: str = self.request.query_params.get('sortDir', "")

        sort = sort_dir = "" if sort_dir == "ASC" else "-"
        sort += sort_field

        return Merchant.objects.filter(user_id=user_id).order_by(sort)

    def perform_create(self, serializer):
        try:
            serializer.save(user=self.request.user)
        except IntegrityError:
            raise ValidationError({'detail': 'A merchant with that name already exists'})
    
    def perform_update(self, serializer):
        try:
            return super().perform_update(serializer)
        except IntegrityError:
            raise ValidationError({'detail': 'A merchant with that name already exists'})
