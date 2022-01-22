from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from testutils import faker
from testutils import get_user_or_create


class AuthTest(APITestCase):

    def login(self, password='testpassword'):
        url = reverse('login')
        user = get_user_or_create(username=faker.name(), password=password)
        data = {'username': user.username, 'password': password}
        return user, self.client.post(url, data)

    def test_login(self):
        user, response = self.login()
        token = Token.objects.get(user=user)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.json())
        self.assertEqual(token.key, response.json()['token'])
        
    def test_logout(self):
        user, login_response = self.login()
        old_token = login_response.json()['token']

        url = reverse('logout')
        response = self.client.delete(url, HTTP_AUTHORIZATION=f'Token {old_token}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        with self.assertRaises(Token.DoesNotExist):
            Token.objects.get(user=user)
        
