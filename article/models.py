from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=120, blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1
            #unique slug
            while Article.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail", kwargs={'slug': self.slug})


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name="comments", on_delete=models.CASCADE)
    writer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment by {self.writer} on {self.article}"

    def get_absolute_url(self):
        return self.article.get_absolute_url()