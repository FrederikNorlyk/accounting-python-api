from rest_framework import viewsets
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from accounting.serializers.user_serializer import UserSerializer
from accounting.utils.demo_data_util import DemoDataUtil


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        validated_data['password'] = make_password(validated_data['password'])

        super().perform_create(serializer)

        user = User.objects.filter(username=validated_data['username'])[0]
        util = DemoDataUtil()
        util.create_demo_data(user)
        
