from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.

#write index, for every view you create with django need to pass a parameter named "request"
def index(request):
    posts = Post.objects.all() #get all post from index page
    return render(request, 'index.html',{'posts':posts}) #render(request, index page, {parameter})

def post(request, slug):
    print(slug)
    posts = Post.objects.all()
    #return index page render_to_response('name of html template we want to load', {object})
    return render(request, 'post.html', {
        'post': get_object_or_404(Post, slug=slug),
        'posts': posts
    })

def about(request):
    return render(request, 'about.html', {})

