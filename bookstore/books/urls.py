from django.urls import path
from . import views

urlpatterns = [
    path('', views.BooksView.as_view(), name='home'),
    path('search/', views.Search.as_view(), name='search'),
    path('delivery', views.delivery, name='delivery'),
    path('about', views.about, name='about'),
    path('<slug:slug>/', views.BooksDetailsView.as_view(), name='book_detail'),
    path('review/<int:pk>', views.AddReview.as_view(), name='add_review'),
    # path('sign_in', views.sign_in, name="sign_in"),
    # path('new_books', views.new_books, name='new_books')

]