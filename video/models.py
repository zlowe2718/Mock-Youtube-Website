from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User, AbstractUser
# Create your models here.

#extends the User model to have more functionality
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	bio =  models.TextField(max_length=500, blank=True)
	profile_pic = models.FileField(upload_to="profile_pictures")
	tag_line = models.CharField(max_length=100, help_text="Enter a small tidbit about you!")
	slug = models.SlugField(null=False, unique=True)

	#gets the URL for the video display page
	def get_absolute_url(self):
		return reverse('profile-detail', kwargs={"slug":self.slug})

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.user.username)
		return super().save(*args, **kwargs)

#Creates the Video Model
class Video(models.Model):
	title = models.CharField(max_length=100, help_text = 'Enter the title for the video')
	file = models.FileField(upload_to="video/", help_text = 'Upload a video file')
	views = models.IntegerField()
	date_uploaded = models.DateField(null=True, blank=True)
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	likes = models.ManyToManyField(User, blank=True, related_name='video_likes')
	dislikes = models.ManyToManyField(User, blank=True, related_name='video_dislikes')
	def __str__(self):
		return self.title

	#gets the URL for the video display page
	def get_absolute_url(self):
		return reverse('video-detail', args=[str(self.id)])

	def total_likes(self):
		return self.likes.count()

	def total_dislikes(self):
		return self.dislikes.count()


#Creates the Comment Model
class Comment(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
	text = models.TextField(max_length=1000, help_text="Enter your comment")
	video = models.ForeignKey('Video', on_delete=models.SET_NULL, null=True)
	date_uploaded = models.DateField(null=True, blank=True)
	likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
	dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')
	def __str__(self):
		return self.text

	def total_likes(self):
		return self.likes.count()

	def total_dislikes(self):
		return self.dislikes.count()

