from django.urls import path
from .views import PostListCreateView, AvaliationCreateView, ComentarioListCreateView, ComentarioDetailView, PostDetailView, AvaliationDetailView

urlpatterns = [
    
    path('posts/', PostListCreateView.as_view(), name='posts-list-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('avaliations/', AvaliationCreateView.as_view(), name='create-avaliation'),
    path('avaliations/<int:post_id>', AvaliationDetailView.as_view(), name='avaliation-detail'),
    path('comentarios/', ComentarioListCreateView.as_view(), name='list-create-comentario'),
    path('comentarios/<int:post>', ComentarioDetailView.as_view(), name='list-create-comentario'),
]
