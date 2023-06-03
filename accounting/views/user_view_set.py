from rest_framework import viewsets
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from accounting.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        validated_data['password'] = make_password(validated_data['password'])
        super().perform_create(serializer)