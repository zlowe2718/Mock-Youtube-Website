from django.urls import path, re_path
from video import views

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:pk>', views.post_video_detail_view, name='video-detail'),
	path('profile/<slug:slug>/', views.profile_detail_view, name='profile-detail'),
]