from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Video, Comment, Profile
from django.contrib.auth.models import User
from django.views import generic
from django.db.models import Count
from .forms import CommentForm
import datetime
from django.http import JsonResponse
from video import functions
# Create your views here.

def index(request):
	video = Video.objects.annotate(num_of_comments=Count('comment'))

	if request.method == 'POST':
		#chnage to ajax call to keep site from refreshing on failed login?
		if "username" in request.POST:
			functions.login_user(request)


	context = {
		"video": video,
	}

	return render(request, 'index.html', context=context)

def post_video_detail_view(request, pk):
	video = Video.objects.get(pk=pk)	
	if request.method == 'POST':
		cf = CommentForm(request.POST)
		if cf.is_valid():
			comment = cf.save(commit=False)
			comment.user = request.user
			comment.video = video
			comment.likes=0
			comment.dislikes=0
			comment.date_uploaded = datetime.datetime.today()
			comment.save()

		if request.accepts("text/javascript"):
			#add comment like functionality here
			content = request.POST.get('content')
			if content == "video-like":
				content_video = video
				if content_video.likes.filter(id=request.user.id).exists(): #already liked the content
					content_video.likes.remove(request.user) #remove user from likes 
					liked=False
				else:
					content_video.likes.add(request.user) 
					liked=True
				context={"likes_count":content_video.total_likes(),"liked":liked,"content_id":"video-like"}
				return JsonResponse(context)
			elif content == "video-view":
				content_video = video
				video.views += 1
				video.save()
			elif content == "search-video":
				search_text = request.POST.get('search-text')
				top_five_videos = functions.getVideos(search_text)
				video_list = []
				for video in top_five_videos:
					video_list.append({"video": video.title, "url": video.get_absolute_url()})
				context = {"video_list": video_list}
				return JsonResponse(context)
	else:
		cf = CommentForm()
	
	video_likes = video.likes
	already_liked=[]
	id=request.user.id
	if (video_likes.filter(id=id).exists()): #puts liked video into list
		already_liked.append(video_likes.get(id=id))
	context = {
		'form': cf,
		'video': video,
		'video_likes': video_likes.count(),
		'already_liked': already_liked,
	}
	return render(request, 'video_detail.html', context)


def profile_detail_view(request, slug):

	context = {
		'profile': Profile
	}

	return render(request, 'profile_detail.html', context)


