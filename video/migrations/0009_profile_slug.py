# Generated by Django 4.0.4 on 2022-06-01 22:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0008_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default={'slug': models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)}, unique=True),
        ),
    ]