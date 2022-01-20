from django.db import models


class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default='')

    class Meta:
        ordering = ['created']
