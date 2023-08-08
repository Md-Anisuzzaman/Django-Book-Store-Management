from django import forms
from Book_store_app.models import BookStoreModel


class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        # exclude = ['first_sub','last_sub']
        fields = ['id', 'book_name', 'author', 'category']
