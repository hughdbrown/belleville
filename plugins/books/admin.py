from django.contrib import admin

from belleville.plugins.books.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_last_name', 'author_first_name', 'status', 'rating',)
    list_filter = ('status', 'rating',)


