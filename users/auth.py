from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

from users.serializers import UserSerializer
from users.serializers import RegisterSerializer
from users.serializers import LogoutSerializer


class LogoutView(GenericAPIView):

    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        """
        Delete existing token
        """
        token = Token.objects.get(user=request.user)
        token.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegisterView(GenericAPIView):

    serializer_class = RegisterSerializer

    def post(self, request):
        """
        Create a new user with a token
        """
        allow_register = getattr(settings, 'ALLOW_REGISTER', False)
        if not allow_register:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)