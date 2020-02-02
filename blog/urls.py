from django.contrib import admin
from django.urls import path
from main.views import index
from about.views import about
from post.views import post
from contact.views import contact

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('post/', post, name='post'),
    path('contact/', contact, name='contact'),
]
