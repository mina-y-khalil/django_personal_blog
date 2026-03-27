from django.urls import path
from . import views


urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts", views.posts, name="posts"),
    path("post/<slug:slug>", views.post_detail, name="post_detail") #the slug here makes sure that the url is unique for each post and it is more readable than using the id of the post
]
