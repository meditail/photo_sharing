from django.db import models

# Create your models here.
class Artwork(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    downloads = models.IntegerField(default=0)
    upload_Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
