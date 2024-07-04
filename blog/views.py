from django.shortcuts import render
from blog.models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by("-published_date")
    return render(request, "blog/post_list.html", {'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def posts_by_author(request, author_id):
    posts = Post.objects.filter(author_id=author_id)
    return render(request, 'posts_by_author.html', {'posts': posts})