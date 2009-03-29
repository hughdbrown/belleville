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
    posts = Post.objects.filter(publish=1).order_by('-created_at')
    month_list = []
    for post in posts:
        post.month = datetime.datetime(post.created_at.year, post.created_at.month, 1)
        month_list.append(post.month)
    months = set(month_list)
    months = list(months)
    months.sort(reverse=True)
    return {'months': months}
register.inclusion_tag('date_list.html')(sidebar_date_list)

 
