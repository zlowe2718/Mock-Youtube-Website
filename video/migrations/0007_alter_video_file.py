# Generated by Django 4.0.4 on 2022-05-20 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0006_alter_video_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(help_text='Upload a video file', upload_to='video/'),
        ),
    ]