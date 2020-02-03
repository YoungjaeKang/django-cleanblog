from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'contents', 'dateCreate',)

admin.site.register(Post, PostAdmin)