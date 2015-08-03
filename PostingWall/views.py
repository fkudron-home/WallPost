from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import IntegrityError
# Create your views here.
from .models import WallPost, User

def index(request):
    "Index view. It's supposed to be main page..."
    content = WallPost.objects.order_by('-pubdate')[:5]
    return render(request, 'PostingWall/index.html', {'content': content,})

def make_post(request):
    "Add post to database"
    post = WallPost(pubdate = timezone.now(), content=request.POST['content_field'], author=request.POST['name_field'])
    post.save()
    return HttpResponseRedirect(reverse('posting_wall:index'))

def register_form(request):
    ""
    return render(request, 'PostingWall/register_form.html')

def register(request):
    ""
    user = User(join_date = timezone.now(), username=request.POST['username_field'],
                password = request.POST['password_field'])
    try:
        user.save()
    except IntegrityError:
        return render(request, 'PostingWall/register_form.html',
                {
                    'error_text' : 'This Username is already taken!',
                    'given_username' : request.POST['username_field'],
                })

    return HttpResponseRedirect(reverse('posting_wall:index'))