from django.contrib.auth.models import User
from rest_framework import serializers

from note.models import Note


class UserSerializer(serializers.ModelSerializer):
    notes = serializers.PrimaryKeyRelatedField(many=True, queryset=Note.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'notes')


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False)
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
