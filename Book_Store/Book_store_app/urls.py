from django.urls import path, include

from .views import home, create, show_book,edit_book,delete_book

urlpatterns = [
    path('', home,  name='homepage'),
    path('create_book/', create,  name='createbookpage'),
    path('show_book/', show_book,  name='showbookpage'),
    path('edit_book/<int:id>', edit_book,  name='editbookpage'),
    path('delete_book/<int:id>', delete_book,  name='deletebookpage'),
]
