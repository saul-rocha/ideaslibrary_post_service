from django.db import models
from datetime import datetime
from django.conf import settings

class Post(models.Model):
    username = models.CharField(max_length=100, default='anonimo')
    nm_livro = models.CharField(max_length=100, default='')
    review = models.TextField(blank=False)
    link = models.CharField(max_length=100, blank=True)
    image = models.ImageField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
    avaliation = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Avaliation(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Comentario(models.Model):

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    comentario = models.TextField()

    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.username
