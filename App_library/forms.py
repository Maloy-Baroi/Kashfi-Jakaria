from django.contrib.auth.forms import forms
from App_library.models import *


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class BookBorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        exclude = ['qty', 'date', 'status']


class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'cover', 'author', 'description', 'available', 'location']


class AddNewSelf(forms.ModelForm):
    class Meta:
        model = BookLocation
        fields = ['self_no', 'row_no']
