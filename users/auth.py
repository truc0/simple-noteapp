from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.conf import settings

from users.serializers import RegisterSerializer


class LogoutView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        """
        Delete existing token
        """
        token = Token.objects.get(user=request.user)
        token.delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegisterView(GenericAPIView):
    serialzer_class = RegisterSerializer
    
    def post(self, request):
        """
        Create a new user with a token
        """
        allow_register = settings.get('ALLOW_REGISTER', False)
        if not allow_register:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user = User.objects.create_user()