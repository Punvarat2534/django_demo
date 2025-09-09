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
from .models import book_description as book_description

def show(request): 
    #if User.is_authenticated:     
    books = book_detail.objects.raw('SELECT * FROM public.book_detail INNER JOIN public.book_description ON book_description.isbn=book_detail.isbn')
    #books = book_detail.objects.extra(tables=['book_description'],where=["book_description.isbn=book_detail.isbn"]) 
    return render(request,"index.html",{'books_list':books})  
    #else:
      #return redirect('/login') 

def detail(request, id): 
    #books = book_detail.objects.get(pk=id)
    books = book_detail.objects.raw("SELECT * FROM public.book_detail INNER JOIN public.book_description ON book_description.isbn=book_detail.isbn where book_detail.id=%s",[id])[0]
    return render(request, 'edit.html', {'books': books})

def insert(request): 
    return render(request,'create.html')   

def create(request):  

    image = request.FILES["image_s"]
    books =  book_detail()
    books.isbn = request.POST["isbn"]
    books.title = request.POST["title"]
    books.author = request.POST["author"]
    books.year = request.POST["year"]
    books.publisher = request.POST["publisher"]
    books.image_s = 'http://127.0.0.1:8000/media/'+image.name
    books.image_m = 'http://127.0.0.1:8000/media/'+image.name
    books.image_l = 'http://127.0.0.1:8000/media/'+image.name
    books.save()
       
    handle_uploaded_file(image)

    description = book_description()
    description.isbn = request.POST.get("isbn")
    description.description = request.POST.get("description")
    description.save()
    return redirect('/')
      

def handle_uploaded_file(f):  
    with open('media/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():
            destination.write(chunk)  


def update(request, id):  
    obj = Product.objects.get(pk=pk)
    obj.name = "some_new_value"
    obj.save()

#================example query================

#joining QuerySets from the Same Model:=============
#queryset1 = MyModel.objects.filter(field1='value1')
#queryset2 = MyModel.objects.filter(field2='value2')
#combined_queryset = queryset1.union(queryset2)      

#Manual Joins (Advanced/Specific Cases):=============
#results = MyModel.objects.extra(
#tables=['other_table'],
#where=["my_model.id = other_table.my_model_id"]
#)

#results = MyModel.objects.raw('SELECT * FROM my_app_mymodel JOIN my_app_othermodel ON ...')

#authors = Author.objects.prefetch_related('books').all()

#books = book_detail.objects.all()  
#books = book_detail.objects.filter(deleted_at=None).values()
#books = book_detail.objects.filter(deleted_at=None).filter(isbn='0374270325').select_related()
#books = book_detail.objects.get(pk=id)

#books = book_detail.objects.extra(tables=['book_description'],where=["book_description.isbn = book_detail.isbn"]) 

#books = book_detail.objects.extra(
#    selects={'isbn','id','title','author','publisher','year','description'},
#    joins=['INNER JOIN public.book_description ON book_description.isbn = book_detail.isbn'],
#    )
