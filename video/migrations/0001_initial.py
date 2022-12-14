# Generated by Django 4.0.4 on 2022-05-15 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title for the video', max_length=100)),
                ('file', models.FileField(help_text='Upload a video file', upload_to='')),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('views', models.IntegerField()),
                ('date_uplaoded', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
