from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def published_recently(self):
        now = timezone.now()
        return now - timedelta(days=7) <= self.published_date <= now
    
    published_recently.boolean = True
    published_recently.short_description = 'Published Recently?'
    
