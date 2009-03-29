from django.contrib import admin

from belleville.entry.models import Post, Category, PostCategory, Comment

class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {"slug": ("name",)}

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author',)
    list_display = ('title', 'publish', 'created_at',)
    prepopulated_fields = {"slug": ("title",)}
    inlines = [
        PostCategoryInline,
        CommentInline, 
    ]

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'publish', 'fullname', 'email', 'website',)


