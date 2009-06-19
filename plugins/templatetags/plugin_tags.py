from django import template
#from django.core.exceptions import ObjectDoesNotExist

from belleville.plugins.books.models import Book
register = template.Library()

def _library_all():
    return Book.objects.all().order_by('-created_at')

def library_list():
    all_books = _library_all()
    current_books = all_books.filter(status=2)[:1]
    tbr_books = all_books.filter(status=3)[:5]
    past_books = all_books.filter(status=1)[:5]
    return {'current_books': current_books, 'tbr_books': tbr_books, 'past_books': past_books}
register.inclusion_tag('library_list.html')(library_list)

def library_all():
    return {'all_books': _library_all()}
register.inclusion_tag('all_books.html')(library_all)

