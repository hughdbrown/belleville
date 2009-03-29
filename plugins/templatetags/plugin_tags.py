from django import template
from django.core.exceptions import ObjectDoesNotExist

from belleville.plugins.books.models import Book
register = template.Library()

def library_list():
    current_books = Book.objects.filter(status=2).order_by('-created_at')[:1]
    tbr_books = Book.objects.filter(status=3).order_by('-created_at')[:5]
    past_books = Book.objects.filter(status=1).order_by('-created_at')[:5]
    return {'current_books': current_books, 'tbr_books': tbr_books, 'past_books': past_books}
register.inclusion_tag('library_list.html')(library_list)

def library_all():
    all_books = Book.objects.all().order_by('-created_at')
    return {'all_books': all_books}
register.inclusion_tag('all_books.html')(library_all)

