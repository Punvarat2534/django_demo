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
        
        books = book_detail.objects.raw('SELECT * FROM public.book_detail INNER JOIN public.book_description ON book_description.isbn=book_detail.isbn')
        #books = book_detail.objects.extra(tables=['book_description'],where=["book_description.isbn=book_detail.isbn"]) 
        return render(request,"index.html",{'books_list':books})  
    #else:
      #return redirect('/login') 

def detail(request, id): 
    
    books = book_detail.objects.get(pk=id)
    #books = book_detail.objects.filter(id=id).select_related()

    #books = book_detail.objects.raw("SELECT * FROM public.book_detail INNER JOIN public.book_description ON book_description.isbn=book_detail.isbn where book_detail.id=1")

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


#books = book_detail.objects.extra(tables=['book_description'],where=["book_description.isbn = book_detail.isbn"]) 

#books = book_detail.objects.extra(
#    selects={'isbn','id','title','author','publisher','year','description'},
#    joins=['INNER JOIN public.book_description ON book_description.isbn = book_detail.isbn'],
#    )
