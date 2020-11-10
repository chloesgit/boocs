from django.urls import path
from . import views

app_name="library"

urlpatterns=[
    path("",views.index, name="index"),
    path("book/<int:book_id>",views.detail, name="detail"),
    path('api/books', views.ListBooks.as_view()),
]