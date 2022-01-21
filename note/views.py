from note.models import Note
from note.serializers import NoteSerializer
from note.permissions import IsOwner

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated, IsOwner]
