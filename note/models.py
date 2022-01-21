from django.db import models


class Note(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, default='')
    owner = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created']
