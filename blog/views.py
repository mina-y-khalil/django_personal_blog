from django.shortcuts import render
from .models import Post

# Create your views here.
def starting_page(request):
    return render(request, 'blog/index.html')



def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    return render(request, 'blog/all-posts.html', {'posts': all_posts})



def post_detail(request, slug):
    pass