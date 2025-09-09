from django.contrib import admin
from django.urls import include, path
from lrc import views as lrc
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',  lrc.show, name='show'),
    path('show',  lrc.show, name='show'),
    path('books/detail/<int:id>', lrc.detail, name='detail'),
    path('books/create', lrc.create, name='create'),
    path('insert',  lrc.insert, name='insert'),
]

if settings.DEBUG:
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)