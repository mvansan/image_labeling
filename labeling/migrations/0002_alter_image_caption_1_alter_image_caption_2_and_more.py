# Generated by Django 4.2.11 on 2024-10-11 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labeling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='caption_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='caption_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='caption_3',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='caption_4',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='caption_5',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='image_url',
            field=models.URLField(unique=True),
        ),
    ]