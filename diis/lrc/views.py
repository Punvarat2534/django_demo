from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.postgres.search import SearchVector
from datetime import date
from .models import book_detail as book_detail
from .forms import BookForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def show(request): 
  
    #if User.is_authenticated: 
        books = book_detail.objects.all()  
        return render(request,"index.html",{'books_list':books})  
        #return render(request,"index.html",{'citizens_list':citizens})  
    #else:
      #return redirect('/login') 

def detail(request, id): 
    books = book_detail.objects.get(pk=id)
    return render(request,"edit.html",{'books':books})  

def create(request):  
    if request.method == "POST":  
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            try: 
                handle_uploaded_file(request.FILES["image_s"])
                form.image_s = "localhost"
                form.save()  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = BookForm()  
    return render(request,'create.html',{'form':form})  

def handle_uploaded_file(f):  
    with open('lrc/uploads/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():
            destination.write(chunk)  