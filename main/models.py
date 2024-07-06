from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField( max_length=100)
    banner = models.ImageField(upload_to='banner')
    intro = models.TextField()
    discription = models.TextField()
    iframe = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='image', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    