from django.contrib import admin
from .models import *


@admin.register(Post)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title", "author","created_at"]