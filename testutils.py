from faker import Faker
from django.contrib.auth.models import User

from note.models import Note


faker = Faker()


def get_user_or_create(username='testuser', password='testpassword'):
    try:
        user = User.objects.get(username=username, password=password)
        return user
    except User.DoesNotExist:
        return User.objects.create_user(username=username, password=password)


def create_random_note(owner):
    return Note.objects.create(
        title=faker.name(), 
        content=faker.name(),
        owner=owner
    )