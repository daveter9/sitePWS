from django.db import models

class Images(models.Model):
    url = models.CharField(max_length=256)
    image_name = models.CharField(max_length=256)

    def __str__(self):
        return self.image_name

    class Meta:
        verbose_name_plural = 'images'