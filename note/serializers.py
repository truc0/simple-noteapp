from rest_framework import serializers
from note.models import Note

class NoteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Note
        fields = ['id', 'title', 'content', 'created', 'updated', 'owner']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)