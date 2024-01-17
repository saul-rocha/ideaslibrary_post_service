from rest_framework import generics
from .models import Post, Avaliation, Comentario
from .serializer import PostSerializer, AvaliationSerializer, ComentarioSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        post = serializer.save()


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AvaliationCreateView(generics.CreateAPIView):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer

    def perform_create(self, serializer):
        avaliation = serializer.save()


class AvaliationDetailView(generics.CreateAPIView):
    queryset = Avaliation.objects.all()
    serializer_class = AvaliationSerializer


class ComentarioListCreateView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

    def perform_create(self, serializer):
        comentario = serializer.save()


class ComentarioDetailView(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
