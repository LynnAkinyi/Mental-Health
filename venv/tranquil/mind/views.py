from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import MyModel

def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')

def community(request):
    return render(request, 'community.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def dir(request):
    return render(request, 'dir.html')

def chat(request):
    return render(request, 'chat.html')

def testimonies(request):
    return render(request, 'testimonies.html')

def book(request):
    return render(request, 'book.html')

def book(request):
    if request.method == 'POST':
        appointment = request.POST.get('appointment')
        MyModel.objects.create(appointment = appointment)
        # Redirect to a success page or display a message
    return render(request, 'book.html')
