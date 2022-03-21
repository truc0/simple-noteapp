from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from typing import Tuple

from testutils import faker
from testutils import get_user_or_create, set_allow_register


class AuthTest(APITestCase):

    def login(self, password='testpassword') -> Tuple[User, Response]:
        url = reverse('login')
        user = get_user_or_create(username=faker.name(), password=password)
        data = {'username': user.username, 'password': password}
        return user, self.client.post(url, data)

    def register(self, username: str, password: str) -> Response:
        url = reverse('register')
        data = {'username': username, 'password': password}
        response = self.client.post(url, data)
        return response

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

    def test_unauthenticated_logout(self):
        url = reverse('logout')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_not_allow_register(self):
        set_allow_register(False)
        user_info = {
            'username': faker.user_name(),
            'password': faker.password(),
        }
        response = self.register(
            username=user_info['username'],
            password=user_info['password']
            )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_register(self):
        set_allow_register(True)

        username = faker.user_name()
        password = faker.password()

        response = self.register(username=username, password=password)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user = User.objects.get(username=username)
        self.assertTrue(user.check_password(password))

    def test_register_with_same_name_twice(self):
        set_allow_register(True)
        # basic info
        username = faker.user_name()
        password1 = faker.password()
        password2 = faker.password()
        # register
        response = self.register(username=username, password=password1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # register with same username again
        response = self.register(username=username, password=password2)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # check if the password changed
        user = User.objects.get(username=username)
        self.assertTrue(user.check_password(password1))

    def test_change_passwords(self):
        url = reverse('change-password')
        old_password = faker.password()
        new_password = faker.password()
        data = {'old_password': old_password, 'new_password': new_password}
        user = get_user_or_create(password=old_password)
        
        self.client.force_authenticate(user=user)
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(user.check_password(old_password))
        self.assertTrue(user.check_password(new_password))

    def test_unauthenticated_change_password(self):
        url = reverse('change-password')
        old_password = faker.password()
        new_password = faker.password()
        data = {'old_password': old_password, 'new_password': new_password}

        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
