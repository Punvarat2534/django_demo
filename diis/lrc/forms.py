from django import forms
from .models import book_detail
from datetime import date

class BookForm(forms.ModelForm):
    class Meta:
        model = book_detail
        fields = ['isbn', 'title', 'author', 'year', 'publisher', 'image_s', 'image_m','image_l']
        id = forms.CharField(label='books_id', max_length=100)
        image_s = forms.FileField()
        widgets = {
            'isbn': forms.TextInput(attrs={
                'class': 'form-control','required': True
            }),
            'title': forms.Textarea(attrs={
                'class': 'form-control','required': True
            }),
             'author': forms.TextInput(attrs={
                'class': 'form-control','required': True
            }), 
            'year': forms.TextInput(attrs={
                'class': 'form-control','required': True
            }), 
            'publisher': forms.TextInput(attrs={
                'class': 'form-control','required': True
            }),
        }
        
        
        #isbn = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
        #isbn = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
        
        #title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'})) 
        #author = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'})) 
        #year = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'})) 
        #publisher = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'})) 
        #image_s = forms.ImageField()
       
        