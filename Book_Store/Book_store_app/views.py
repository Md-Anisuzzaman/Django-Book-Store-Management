from django.shortcuts import render, redirect
from Book_store_app.forms import BookStoreForm
from Book_store_app.models import BookStoreModel

# Create your views here.


def home(request):
    return render(request, 'base.html')


def create(request):
    if request.method == 'POST':
        book = BookStoreForm(request.POST)
        if book.is_valid():
            print(book.cleaned_data)
            book.save(commit=True)
            return redirect('/show_book/')
    else:
        book = BookStoreForm()
    return render(request, 'store_book.html', {'form': book})


def show_book(request):
    book = BookStoreModel.objects.all()
    return render(request, 'show_book.html', {'data': book})


def edit_book(request, id):
    book = BookStoreModel.objects.get(pk=id)
    form = BookStoreForm(instance=book)
    if request.method == 'POST':
        info = BookStoreForm(request.POST, instance=book)
        if info.is_valid():
            info.save()
            return redirect('/show_book/')
    return render(request, 'edit_book.html', {'form': form})


def delete_book(request, id):
    book = BookStoreModel.objects.get(pk=id).delete()
    print("my_book = ",book)
    return redirect('/show_book/')
