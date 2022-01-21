from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from faker import Faker

from note.models import Note


faker = Faker()


def get_user_or_create(username='testuser', password='testpassword'):
    try:
        user = User.objects.get(username=username, password=password)
        return user
    except User.DoesNotExist:
        return User.objects.create(username=username, password=password)


def create_random_note(owner):
    return Note.objects.create(
        title=faker.name(), 
        content=faker.name(),
        owner=owner
    )


class NoteList(APITestCase):
    def test_unauthenticated_note_list(self):
        """
        Ensure list notes need authentication
        """
        url = reverse('note-list')
        data = {'title': 'New Idea'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_note(self):
        url = reverse('note-list')
        user = get_user_or_create(username='testuser')
        another = get_user_or_create(username='another')

        note1 = create_random_note(owner=user)
        note2 = create_random_note(owner=another)

        self.client.force_authenticate(user=another)
        response = self.client.get(url)
        response_data = response.json()

        self.assertEqual(1, len(response_data))
        self.assertDictContainsSubset(
            {'title': note2.title, 'content': note2.content},
            response_data[0]
            )


    def test_create_note(self):
        url = reverse('note-list')
        data = {'title': 'New Idea', 'content': 'Hello world'}
        fields = ('id', 'title', 'content', 'created', 'updated')

        user = get_user_or_create()
        self.client.force_authenticate(user=user)
        response = self.client.post(url, data, format='json')
        response_data = response.json()

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(1, Note.objects.count())
        self.assertEqual(user, Note.objects.last().owner)

        for field in fields:
            self.assertIn(field, response_data)
        self.assertEqual(response_data['id'], Note.objects.first().id)
