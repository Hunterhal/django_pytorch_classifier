from django.db import models

class Image(models.Model):
    image_class = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title