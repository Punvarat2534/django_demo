from django.contrib import admin
from django.urls import include, path
from lrc import views as lrc

urlpatterns = [
    path('',  lrc.show, name='show'),
    path('/books/detail/<int:id>', lrc.detail, name='detail'),

    #path('/',  lrc.members, name='members'),
    #path('members/', lrc.members, name='members'),
    path('admin/', admin.site.urls),
]