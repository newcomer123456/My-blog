from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title

    def published_recently(self):
        return self.published_date >= timezone.now - timedelta(days=7)
    
    published_recently.boolean = True
    published_recently.short_description = 'Published Recently?'
    
