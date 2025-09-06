from datetime import date
from django.db import models
from django.utils import timezone

class book_detail(models.Model):

    id = models.AutoField(primary_key=True)
    isbn = models.CharField("isbn", max_length=30, blank = True, null = True)

    title = models.CharField("title", max_length=100, blank = True, null = True)
    author = models.CharField("author", max_length=50, blank = True, null = True)
   
    year = models.CharField("year", max_length=10, blank = True, null = True)
    publisher = models.CharField("publisher", max_length=50, blank = True, null = True)
    image_s = models.CharField("image_s",max_length=100, blank = True, null = True)
    image_m = models.CharField("image_s",max_length=100, blank = True, null = True)
    image_l = models.CharField("image_s",max_length=100, blank = True, null = True)
    deleted_at = models.DateTimeField("deleted_at", auto_now_add=True)
    
    class Meta:  
        db_table = "book_detail"  

    def __str__(self):
        return self.firstName