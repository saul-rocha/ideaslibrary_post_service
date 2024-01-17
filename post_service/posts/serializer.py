from rest_framework import serializers
from .models import Post, Avaliation, Comentario


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'username', 'nm_livro', 'review', 'link', 'image', 'created_at', 'avaliation']


class AvaliationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliation
        fields = ['post_id', 'username']

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['post', 'username', 'comentario', 'created_at']
