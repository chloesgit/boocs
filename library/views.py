from django.shortcuts import render
from .models import Book

# Create your views here.
def index(request):
    context = {
        "liste": Book.objects.all()
    }
    return render(request, "library/index.html", context)

def detail(request, book_id):
    book = Book.objects.get(pk=book_id)
    context = {"book": book}
    return render(request, "library/detail.html", context)
