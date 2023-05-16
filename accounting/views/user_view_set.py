from rest_framework import viewsets
from django.contrib.auth.models import User

from accounting.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer