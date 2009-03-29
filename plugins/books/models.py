from django.db import models
from django.http import Http404
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

class Book(models.Model):
    """
    """
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )

    STATUS_CHOICES = (
        ('1', 'have read'),
        ('2', 'currently reading'),
        ('3', 'on the pile to be read'),
    )

    title = models.CharField(max_length=255)
    author_first_name = models.CharField(max_length=255)
    author_last_name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255)
    status = models.IntegerField(max_length=2, blank=True, null=True, choices=STATUS_CHOICES)
    rating = models.IntegerField(max_length=2, blank=True, null=True, choices=RATING_CHOICES)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return "http://www.powells.com/partner/33557/biblio/%s/" % self.isbn

    def __unicode__(self):
        return u"%s" % self.title

    class Meta:
        ordering = ['status']

