# Generated by Django 5.1.2 on 2024-10-21 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeling', '0004_remove_image_image_file_image_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_url',
        ),
        migrations.AddField(
            model_name='image',
            name='image_file',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]