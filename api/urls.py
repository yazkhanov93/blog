from django.urls import path
from api.articles.views import *


urlpatterns = [
    path("posts/", PostList.as_view(), name="posts"),
    path("post/<int:pk>/", PostDetail.as_view(), name="post"),
]