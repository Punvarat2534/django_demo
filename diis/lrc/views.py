from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.postgres.search import SearchVector
from datetime import date
from .models import book_detail as book_detail

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