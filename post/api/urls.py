from django.urls import path, include
from rest_framework.routers import SimpleRouter

from post.api import viewsets, views

router = SimpleRouter()
router.register(r'posts', viewsets.PostViewset, basename='post')
router.register(r'comments', viewsets.CommentViewset, basename='comment')


urlpatterns = [
    path('ping/', views.PingView.as_view(), name='ping'),
] + router.get_urls()
