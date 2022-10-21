from django.contrib import admin
from .models import Book, Category, Reviews, Genre


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'url')
#     list_display_links = ('name',)


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'url': ('title',)}


admin.site.register(Book, BookAdmin)
admin.site.register(Category)
admin.site.register(Reviews)
admin.site.register(Genre)
