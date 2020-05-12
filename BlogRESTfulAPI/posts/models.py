from django.db import models

# Create your models here.
class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    post = models.TextField()
    tags = models.CharField(max_length=100)
    imgurl = models.CharField(max_length=100)

    class Meta:
        ordering = ['created']