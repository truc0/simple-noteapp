from .models import Note
from .serializers import NoteSerializer
from .permissions import IsOwner

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
