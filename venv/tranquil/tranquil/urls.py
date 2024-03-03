"""
URL configuration for tranquil project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mind.views import index
from mind.views import home
from mind.views import community
from mind.views import blog
from mind.views import about
from mind.views import login
from mind.views import dir
from mind.views import chat
from mind.views import testimonies
from mind.views import book

from django.urls import include


urlpatterns = [
    path('', index, name='index'),
    path('home.html/', home, name='home'),  # Replace "home" with a valid view function or path
    path('community.html/', community, name='community'),
    path('community.html/chat.html', chat, name='chat'),
    path('community.html/dir.html', dir, name='dir'),
    path('community.html/book.html', book, name='book'),
    path('community.html/home.html', home, name='home'),
    path('community.html/testimonies.html', testimonies, name='testimonies'),
    path('blog.html/', blog, name='blog'),
    path('about.html/', about, name='about'),
    path('login.html/', login, name='login'),
    path('admin.html/', admin.site.urls),
    path('dir.html/', dir, name='dir'),
    path('chat.html/', chat, name='chat'),
    path('testimonies.html/', testimonies, name='testimonies'),
    # path('home.html/profile.html', profile, name='book'),
    path('home.html/community.html', community, name='book'),
    path('home.html/blog.html', blog, name='blog'),
    path('home.html/about.html', about, name='about'),
    path('home.html/dir.html', dir, name='dir'),
    path('home.html/chat.html', chat, name='chat'),
    path('home.html/testimonies.html', testimonies, name='testimonies'),
    # path('home.html/logout.html', logout, name='book'),
]
