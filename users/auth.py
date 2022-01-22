from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings


class LogoutView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        """
        Delete existing token
        """
        token = Token.objects.get(user=request.user)
        token.delete()  
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class RegisterView(GenericAPIView):
    ...