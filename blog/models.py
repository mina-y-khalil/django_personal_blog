from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.TextField(max_length=300)
    slug = models.SlugField(unique=True)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True)

    def __str__(self):
        return self.title
