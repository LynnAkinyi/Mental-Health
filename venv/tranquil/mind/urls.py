from django.urls import path
from mind.views import index
from mind.views import home
from mind.views import community
from mind.views import dir
from mind.views import chat
from mind.views import testimonies
from mind.views import book


from . import views

urlpatterns = [
    path('', index, name='index'),
    path('home.html/', views.home, name='home'),  # Replace "home" with a valid view function or path
    path('community.html/', views.community, name='community'),
    path('community.html/chat.html', views.chat, name='chat'),
    path('community.html/dir.html', views.dir, name='dir'),
    path('community.html/book.html', views.book, name='book'),
    path('community.html/home.html', views.home, name='home'),
    path('community.html/testimonies.html', views.testimonies, name='testimonies'),
    path('blog.html/', views.blog, name='blog'),
    path('about.html/', views.about, name='about'),
    path('dir.html/', views.dir, name='dir'),
    path('chat.html/', views.chat, name='chat'),
    path('testimonies.html/', views.testimonies, name='testimonies'),
    path('home.html/book.html', views.book, name='book'),
    path('home.html/dir.html', views.dir, name='dir'),
    path('home.html/community.html', views.community, name='community'),
    # path('home.html/profile.html', views.profile, name='profile'),
    path('home.html/blog.html', views.blog, name='blog'),
    path('home.html/about.html', views.about, name='about'),
    path('home.html/chat.html', views.chat, name='chat'),
    path('home.html/testimonies.html', views.testimonies, name='testimonies'),
    # path('home.html/logout.html', views.logout, name='logout'),
]
