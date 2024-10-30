from django.db import models

class Image(models.Model):
    image_url = models.URLField(blank=True, null=True) 
    caption_1 = models.CharField(max_length=255, blank=True, null=True)
    caption_2 = models.CharField(max_length=255, blank=True, null=True)
    caption_3 = models.CharField(max_length=255, blank=True, null=True)
    caption_4 = models.CharField(max_length=255, blank=True, null=True)
    caption_5 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.image_url) if self.image_url else "No Image"
