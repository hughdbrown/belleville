from django.db import models
from django.http import Http404
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Post(models.Model):
    """
    basic blog entry model - 
    entries can only be posted from the admin, 
    active (publish) defaults to false
    """
    author = models.ForeignKey(User)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True, editable=False)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return u"%s" % self.title

    def get_absolute_url(self):
        return "/view/%s/" % self.slug

    class Meta:
        ordering = ['-created_at']

class Category(models.Model):
    """
    blog entry categories, created in admin only
    """
    name = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return u"%s" % self.name

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "categories"

class PostCategory(models.Model):
    """
    category to blog entry assignment
    """
    post = models.ForeignKey(Post)
    category = models.ForeignKey(Category)

    class Meta:
        verbose_name_plural = "post categories"

class Comment(models.Model):
    """
    """
    post = models.ForeignKey(Post)
    fullname = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    website = models.URLField(verify_exists=True, max_length=255, blank=True)
    body = models.TextField()
    publish = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"%s" % self.id

    class Meta:
        ordering = ['-created_at']

    # custom method to clean website - make sure it's a complete url


from django.contrib.comments.signals import comment_was_posted

def on_comment_was_posted(sender, comment, request, *args, **kwargs):
    # spam checking can be enabled/disabled per the comment's target Model
    #if comment.content_type.model_class() != Entry:
    #    return

    from django.contrib.sites.models import Site
    from django.conf import settings

    try:
        from akismet import Akismet
    except:
        return

    ak = Akismet(
        key=settings.AKISMET_API_KEY,
        blog_url='http://%s/' % Site.objects.get(pk=settings.SITE_ID).domain
    )

    if ak.verify_key():
        data = {
            'user_ip': request.META.get('REMOTE_ADDR', '127.0.0.1'),
            'user_agent': request.META.get('HTTP_USER_AGENT', ''),
            'referrer': request.META.get('HTTP_REFERER', ''),
            'comment_type': 'comment',
            'comment_author': comment.user_name.encode('utf-8'),
        }

        if ak.comment_check(comment.comment.encode('utf-8'), data=data, build_data=True):
            comment.flags.create(
                user=comment.content_object.author,
                flag='spam'
            )
            comment.is_public = False
            comment.save()

comment_was_posted.connect(on_comment_was_posted)

