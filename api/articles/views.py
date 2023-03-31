from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from articles.models import Post
from .serializers import *


class PostList(APIView):
    def get(self, request):
        try:
            posts = Post.objects.all().only("id","title", "image","author","created_at")
            if request.query_params.get("title", None):
                title = request.query_params.get("title",None)
                posts = posts.filter(title__icontains=title)
            serializer = PostsSerializer(posts, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PostDetail(APIView):
    def get(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
            serializer = PostSerializer(post, many=False)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)