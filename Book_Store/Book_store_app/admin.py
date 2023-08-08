from django.contrib import admin
from Book_store_app.models import BookStoreModel

# Register your models here.

class BookStoreModelAdmin(admin.ModelAdmin):
    list_display =("id", "book_name", "author","category","first_sub","last_sub")

admin.site.register(BookStoreModel,BookStoreModelAdmin)