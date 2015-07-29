from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
# Create your views here.
from .models import WallPost

def index(request):
    "Index view. It's supposed to be main page..."
    content = WallPost.objects.order_by('-pubdate')[:5]
    return render(request, 'PostingWall/index.html', {'content': content,})

def make_post(request):
    "Add post to database"
    post = WallPost(pubdate = timezone.now(), content=request.POST['content_field'], author=request.POST['name_field'])
    post.save()
    return HttpResponseRedirect(reverse('posting_wall:index'))