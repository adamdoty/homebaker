from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Treat(models.Model):
    """A baked good the user has made before or plans to make."""
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(max_length=50)
    cover_img = models.URLField(blank=True, null=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    # rating field = in a review, the recipient user gives a rating. this is the overall rating from all review ratings
    rating = models.TextField(default="⭐⭐⭐⭐⭐")

    class Meta:
        ordering = ['rating', 'created']
        indexes = [
            models.Index(fields=['rating']),
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return self.title


class Note(models.Model):
    """Details about a Treat, treat recipe, or other aspect of a treat."""
    treat = models.ForeignKey(Treat, on_delete=models.CASCADE, related_name='notes')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return f'Note on {self.treat}'

# class Comment(models.Model):
#     treat = models.ForeignKey(Treat, on_delete=models.CASCADE)
#     body = models.TextField()
#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#
#
# class Review(models.Model):
#     treat = models.ForeignKey(Treat, on_delete=models.CASCADE)
#     body = models.TextField()
#     rating = models.IntegerField()
#     publish = models.DateTimeField(default=timezone.now)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
