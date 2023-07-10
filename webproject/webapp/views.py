from django.http import HttpResponse
from django.shortcuts import render, redirect

from webapp.models import books
from .forms import bookform


# Create your views here.
def index(request):
    var = books.objects.all()
    context = {
        'books_list': var
    }
    return render(request, 'index.html', context)


def details(request, book_id):
    book = books.objects.get(id=book_id)
    return render(request, "detail.html", {'book': book})


def book_add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        year = request.POST.get('year')
        img = request.FILES['img']
        book = books(name=name, desc=desc, year=year, img=img)
        book.save()
    return render(request, 'add.html')


def update(request, id):
    book = books.objects.get(id=id)
    form = bookform(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'edit.html', {'form': form, 'book': book})


def delete(request, id):
    if request.method == 'POST':
        book = books.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request, 'delete.html')
