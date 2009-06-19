from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template.loader import render_to_string

from belleville.entry.models import Post, Category, PostCategory, Comment
from belleville.entry.forms import CommentForm

def list_all(request):
    """
    
    """
    template_name = 'all.html'
    list_all = Post.objects.filter(publish=True).order_by('-created_at')
    for entry in list_all:
        entry.category_list = Category.objects.filter(postcategory__post__pk=entry.id)
    context = {'entry_list': list_all }
    return render_to_response(template_name, context, context_instance=RequestContext(request))

def list_entries(request, category=None, username=None, date=None):
    """
    List all entries, paginated
    """
    template_name = 'list.html'
    context = {}
    per_page = 5
    page = int(request.GET.get('page', '1'))

    if category:
        context['category'] = category
        grouped_list = entries_by_category(request, category)
    elif username:
        context['author'] = username
        try:
            user = User.objects.get(username=username)
            grouped_list = Post.objects.filter(author=user.id).order_by('-created_at')
        except ObjectDoesNotExist:
            grouped_list = None
    elif date:
        context['date'] = date
        grouped_list = Post.objects.filter(created_at__startswith=date, publish=True).order_by('-created_at')
    else:
        grouped_list = Post.objects.filter(publish=True).order_by('-created_at')

    for entry in grouped_list:
        entry.category_list = Category.objects.filter(postcategory__post__pk=entry.id)
        entry.comments = Comment.objects.filter(post=entry.id)

    total_entries = grouped_list.count()
    total_pages = (total_entries/per_page)+1
    context['page_range'] = range(1, total_pages+1)

    offset = (page * per_page) - per_page
    limit = offset + per_page
    entry_list = grouped_list[offset:limit]
    context['entry_list'] = entry_list

    return render_to_response(template_name, context, context_instance=RequestContext(request))

def viewid(request, id):
    """
    """
    try:
        commented_entry = Post.objects.get(pk=id, publish=True)
        title = commented_entry.slug
        return HttpResponseRedirect('/view/%s/' % title)
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')	

def view(request, title, form_class=CommentForm):
    """
    """
    template_name = 'view.html'
    context = {}

    try:
        entry = Post.objects.get(slug=title, publish=True)
    except ObjectDoesNotExist:
        entry = None

    if entry:
        try:
            entry.category_list = Category.objects.filter(postcategory__post__pk=entry.id)
            entry.body = str(entry.body)
        except ObjectDoesNotExist:
            entry.category_list = None

        if request.method == 'POST':  # new comment
            form = form_class(request.POST)
            print form
            if form.is_valid():
                form.post_id = entry.id
                form.publish = True
                form.save()
                # from django.core.mail import send_mail
		# email_dict = { 'fullname': request.POST['fullname'], 'email': request.POST['email'], 
		# 		'website': request.POST['website'], 'body': request.POST['body'], 'post': request.POST['post'] }
                # email_dict['site'] = Site.objects.get_current()
		# email_dict['title'] = title
                # subject = str(request.POST['fullname'])+" has just posted a comment"
                # message = render_to_string('comment_notification.txt', email_dict)
		# print settings.ADMIN_EMAIL
                # send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [settings.ADMIN_EMAIL])
                # to do: confirmation that comment is being reviewed
                return HttpResponseRedirect('/view/%s/' % title)
        else:
            form = form_class()

        context['entry'] = entry
        context['comment_list'] = comments(request, entry.id)
        context['form'] = form

    return render_to_response(template_name, context, context_instance=RequestContext(request))

def preview(request, title, form_class=CommentForm):
    """
    """
    template_name = 'view.html'
    context = {}

    try:
        entry = Post.objects.get(slug=title)
    except ObjectDoesNotExist:
        entry = None

    if entry:
        try:
            entry.category_list = Category.objects.filter(postcategory__post__pk=entry.id)
            entry.body = str(entry.body)
        except ObjectDoesNotExist:
            entry.category_list = None

        if request.method == 'POST':
            form = form_class(request.POST)
            if form.is_valid():
                form.post_id = entry.id
                form.save()
                return HttpResponseRedirect('/view/%s/' % title)
        else:
            form = form_class()

        context['entry'] = entry
        context['comment_list'] = comments(request, entry.id)
        context['form'] = form

    return render_to_response(template_name, context, context_instance=RequestContext(request))

def comments(request, entry_id):
    """
    """
    if entry_id:
        try:
            comment_list = Comment.objects.filter(post=entry_id, publish=True).order_by('created_at')
            for comment in comment_list:
                comment.body = str(comment.body)
        except ObjectDoesNotExist:
            comment_list = None
    return comment_list

def entries_by_category(request, category):
    try:
        post_category = Category.objects.get(slug=category)
    except ObjectDoesNotExist:
        post_category = None
    if post_category: entry_list = Post.objects.filter(postcategory__category=post_category.id, publish=True).order_by('-created_at')
    return entry_list

