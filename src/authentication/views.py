from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, CustomTokenObtainPairSerializer


class UserListCreateAPIView(generics.ListCreateAPIView):
    """ View for listing and creating users """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class CustomTokenObtainPairView(TokenObtainPairView):
    """ Custom view for obtaining JWT authentication tokens """
    serializer_class = CustomTokenObtainPairSerializer
