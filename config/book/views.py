from django.shortcuts import render

from .models import Book
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = "book_list.html"
    context_object_name = "books"

class BookCreateView(CreateView):
    model = Book
    template_name = "book_form.html"
    fields = "__all__"
    success_url = reverse_lazy("book-list")

class BookDeleteView(DeleteView):
    model = Book
    template_name = "book_confirm_delete.html"
    success_url = reverse_lazy("book-list")

class BookUpdateView(UpdateView):
    model = Book
    template_name = "book_form.html"
    fields = "__all__"
    success_url = reverse_lazy("book-list")

class BookDetailView(DetailView):
    model = Book
    template_name = "book_detail.html"
    context_object_name = "book"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["smile"] = "👾👾👾👾👾👾👾👾"
        return context
