# Generated by Django 4.0.4 on 2022-06-05 14:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0012_remove_comment_dislikes_remove_comment_likes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='comment_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='comment_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='video',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='video_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='video',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='video_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='LikeButton',
        ),
    ]
