from .models import Video
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def getVideos(search_text):
	top_five_videos = Video.objects.filter(title__icontains = search_text).order_by('title')[:5]
	return top_five_videos

def login_user(request):
	username = request.POST['username']
	password = request.POST['password']

	user = authenticate(request, username=username, password=password)

	if user is not None:
		login(request, user)
	else:
		messages.info(request, 'Invalid Username or Password')

def register_user(request):
	username = request.POST['username']
	password = request.POST['password']
	confirm_password = request.POST['confirm_password']
	email = request.POST['email']

	if password == confirm_password:
		if User.objects.filter(username=username).exists():
			messages.info(request, 'Username is already taken')
		elif User.objects.filter(email=email).exists():
			messages.info(request, 'Email is already taken')
		else:
			user = User.objects.create_user(username=username, password=password, email=email)
			user.save()
	else:
		messages.info(request, "The Confirmation Password does not match")

