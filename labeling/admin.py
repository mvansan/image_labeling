from django.contrib import admin
from .models import Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_url', 'caption_1', 'caption_2', 'caption_3', 'caption_4', 'caption_5')
