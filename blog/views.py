from django.shortcuts import render
from .models import Post

# Create your views here.
def starting_page(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    if not latest_posts:
        latest_posts = dummy_posts[:3]
    return render(request, 'blog/index.html', {'posts': latest_posts})



dummy_posts = [
    {'title': 'My First Post', 'excerpt': 'This is a short excerpt for the first post.', 'slug': 'my-first-post', 'date': 'March 27, 2026', 'content': 'Full content for the first post goes here.', 'image': None},
    {'title': 'Learning Django', 'excerpt': 'Django makes it easy to build web apps quickly.', 'slug': 'learning-django', 'date': 'March 26, 2026', 'content': 'Full content about learning Django goes here.', 'image': None},
    {'title': 'Python Tips', 'excerpt': 'Some useful Python tips and tricks for everyday use.', 'slug': 'python-tips', 'date': 'March 25, 2026', 'content': 'Full content about Python tips goes here.', 'image': None},
]

def posts(request):
    all_posts = Post.objects.all().order_by('-date')
    if not all_posts:
        all_posts = dummy_posts
    return render(request, 'blog/all-posts.html', {'posts': all_posts})



def post_detail(request, slug):
    post = next(post for post in dummy_posts if post['slug'] == slug)
    return render(request, 'blog/post-detail.html', {'post': post})