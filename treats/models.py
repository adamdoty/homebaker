from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Treat(models.Model):
    """A baked good the user has made before or plans to make."""

    class Ratings(models.TextChoices):
        ONE_STAR = 1, '⭐'
        TWO_STARS = 2, '⭐⭐'
        THREE_STARS = 3, '⭐⭐⭐'
        FOUR_STARS = 4, '⭐⭐⭐⭐'
        FIVE_STARS = 5, '⭐⭐⭐⭐⭐'

    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cover_img = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    rating = models.CharField(max_length=1, choices=Ratings.choices,
                              default=Ratings.THREE_STARS)

    class Meta:
        ordering = ['rating', 'created']
        indexes = [
            models.Index(fields=['-rating']),
            models.Index(fields=['created'])
        ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Treat, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Note(models.Model):
    """Details about a Treat, treat recipe, or other aspect of a treat."""
    treat = models.ForeignKey(Treat, on_delete=models.CASCADE, related_name='notes')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        return f'Note on {self.treat}: {self.body[:20]}...'

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
