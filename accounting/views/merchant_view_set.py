from rest_framework import viewsets
from rest_framework import permissions
from accounting.permissions.is_owner import IsOwner

from accounting.serializers.merchant_serializer import MerchantSerializer
from accounting.models.merchant import Merchant


class MerchantViewSet(viewsets.ModelViewSet):
    serializer_class = MerchantSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]


    def get_queryset(self):
        user_id = self.request.user.id
        return Merchant.objects.filter(user_id=user_id).order_by("name")

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    