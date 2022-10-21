from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Book, Category, Genre
from cart.forms import CartAddProductForm


class GenreCategory:
    """Жанры и категории книг """
    model = Book

    def get_genres(self):
        return Genre.objects.all()

    def get_category(self):
        return Category.objects.all()


class BooksView(GenreCategory, ListView):
    """Список книг"""
    model = Book
    queryset = Book.objects.all()
    template_name = 'books/books_list.html'


class BooksDetailsView(GenreCategory, DetailView):
    """Полное описание книги"""
    model = Book
    slug_field = 'url'

    def book_detail(self, pk, slug):
        book = get_object_or_404(Book,
                                 id=pk,
                                 slug=slug,
                                 available=True)
        cart_product_form = CartAddProductForm()
        return render(self, 'books/book_detail.html', {'product': book,
                                                          'cart_product_form': cart_product_form})


class AddReview(GenreCategory, View):
    """Отзывы без регистрации"""
    def post(self, request, pk):
        print(request.POST)
        return redirect('/')


class Search(ListView):
    """Поиск книг"""

    # paginate_by = 8

    def get_queryset(self):
        return Book.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context


def delivery(request):
    return render(request, 'books/delivery.html')


def about(request):
    return render(request, 'books/about.html')





