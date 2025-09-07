from django.contrib import admin
from django.urls import include, path
from lrc import views as lrc

urlpatterns = [
    path('',  lrc.show, name='show'),
    path('show',  lrc.show, name='show'),
    path('books/detail/<int:id>', lrc.detail, name='detail'),
    path('books/create', lrc.create, name='create'),

    
]