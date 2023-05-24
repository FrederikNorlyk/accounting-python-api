from rest_framework import viewsets
from rest_framework import permissions
from accounting.permissions.is_owner import IsOwner

from accounting.serializers.merchant_serializer import MerchantSerializer
from accounting.models.merchant import Merchant


class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all().order_by("name");
    serializer_class = MerchantSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    