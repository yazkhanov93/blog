from django.db import models
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="ady")
    author = models.CharField(max_length=100, verbose_name="awtory", blank=True, null=True)
    image = models.ImageField(upload_to="article_img/", verbose_name="suraty")
    content = RichTextField(verbose_name="Beýany")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Goşulan senesi")

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Makalalar"

    def __str__(self):
        return self.title
