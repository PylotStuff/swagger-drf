from rest_framework.viewsets import ModelViewSet

from post.models import Post, Comment 
from post.api.serializers import PostSerializer, CommentSerializer

class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewset(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
