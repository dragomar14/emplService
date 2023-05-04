from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User
from .serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """API view for creating a new user"""

    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserListAPIView(generics.ListAPIView):
    """API view for listing all users"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """API view for retrieving, updating, or deleting a single user"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class CustomTokenObtainPairView(TokenObtainPairView):
    """Customized token obtain view to return additional user data"""

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.user
        token_data = response.data
        token_data["user_id"] = user.id
        token_data["email"] = user.email
        return response
