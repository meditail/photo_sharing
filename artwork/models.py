from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artwork(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    downloads = models.IntegerField(default=0)
    upload_Date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='artworks', default=None)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
