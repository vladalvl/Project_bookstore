from django.db import models
from django.db.models import SET_NULL
from django.urls import reverse


class Genre(models.Model):
    name = models.CharField("Жанр", max_length=100)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Category(models.Model):
    name = models.CharField("Категория", max_length=100)
    url = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Book(models.Model):
    title = models.CharField('Название', max_length=100)
    author = models.CharField('Автор', max_length=100)
    image = models.ImageField('Изображение', upload_to='books/', null=True)
    description = models.TextField('Описание')
    pages = models.PositiveIntegerField('Кол-во страниц', default=0)
    url = models.SlugField(max_length=150, unique=True, null=True)
    year = models.PositiveSmallIntegerField('Год издания', null=True)
    genre = models.ManyToManyField(Genre, verbose_name='жанры')
    category = models.ManyToManyField(Category, verbose_name='категории')
    price = models.FloatField('Цена', null=True)
    # stock = models.PositiveIntegerField()
    # available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_details', kwargs={'book_id': self.id})

    class Meta:
        ordering = ('title',)
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        index_together = (('id', 'url'), )


class User(models.Model):
    username = models.CharField(max_length=255, default=None)
    password = models.CharField(max_length=255, default=None)
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=17, default=None)
    address = models.CharField(max_length=255, default=None)
    login = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.pk}: {self.username}'


# class Basket(models.Model):
#     book_id = models.IntegerField()
#     book = models.CharField(max_length=255, default=None)
#     price = models.FloatField()
#     amount = models.FloatField()
#     cost = models.FloatField()
#
#     def __str__(self):
#         return f'{self.pk}: {self.book}'


class Order(models.Model):
    user_type = models.CharField(max_length=255, default='Гость')
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=17, default=None)
    address = models.CharField(max_length=255, default=None)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    comment = models.CharField(max_length=510, null=True)
    order_info = models.CharField(max_length=2040)
    user = models.ForeignKey('User', null=True, on_delete=SET_NULL, related_name='заказы')

    def __str__(self):
        return f'Заказ {self.pk}'


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    text = models.TextField('Отзыв', max_length=5000)
    parent = models.ForeignKey('self', verbose_name='Родитель', on_delete=models.SET_NULL, blank=True, null=True)

    book = models.ForeignKey(Book, verbose_name='книга', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


