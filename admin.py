from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.contrib.comments.models import Comment as Comments

from belleville.entry.models import Post, Category, Comment
from belleville.entry.admin import PostAdmin, CategoryAdmin, CommentAdmin

from belleville.plugins.books.models import Book
from belleville.plugins.books.admin import BookAdmin

class AdminSite(admin.AdminSite):
    pass

site = AdminSite()

site.register(User)
site.register(Group)
site.register(Comments)

site.register(Book, BookAdmin)

site.register(Post, PostAdmin)
site.register(Category, CategoryAdmin)
site.register(Comment, CommentAdmin)

