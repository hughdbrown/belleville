import datetime

from django import template
from django.core.exceptions import ObjectDoesNotExist

from belleville.entry.models import Post, Category, PostCategory
register = template.Library()

def sidebar_category_list():
    categories = Category.objects.filter(postcategory__post__publish=1).distinct()
    for category in categories:
        try:
            category.posts = Post.objects.filter(postcategory__category=category.id)
        except ObjectDoesNotExist:
            category.posts = None
    return {'categories': categories}
register.inclusion_tag('category_list.html')(sidebar_category_list)

def sidebar_date_list():
    return {'months': Post.objects.filter(publish=1).dates('created_at', 'month', order='DESC')}
register.inclusion_tag('date_list.html')(sidebar_date_list)

 
