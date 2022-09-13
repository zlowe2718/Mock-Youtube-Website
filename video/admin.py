from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import Video, Comment, Profile

class CommentsInLine(admin.TabularInline):
	model = Comment
	extra = 0

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
	list_display = ('title', 'date_uploaded', 'user')
	inlines = [CommentsInLine]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
	list_display = ('video', 'date_uploaded', 'user')

# Define an inline admin descriptor for Profile model
# which acts a bit like a singleton
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

