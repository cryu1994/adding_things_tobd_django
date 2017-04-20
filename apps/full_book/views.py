from django.shortcuts import render, redirect
from .models import Book

def index(request):
    context = {
        'books' : Book.objects.all()
    }
    return render(request, "index/index.html", context)

def create(request):
    #too lazy to type every time
    req = request.POST
    Book.objects.create(title = req['title'], category = req['category'], author = req['author'])
    return redirect('/')
# Create your views here.
