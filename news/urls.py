from django.urls import path
from news import views

app_name = "news"

urlpatterns = [
    path("create-post", views.PostCreateView.as_view(), name="create-post"),
    path("update-post/<int:pk>", views.PostUpdateView.as_view(), name="update-post"),
    path("delete-post/<int:pk>", views.PostDeleteView.as_view(), name="delete-post"),
    path("show-posts", views.PostsListView.as_view(), name="show-posts"),
    path("create-comment", views.CommentCreateView.as_view(), name="create-comment"),
    path("show-comments", views.CommentListView.as_view(), name="show-comments"),
    path("upvote-post", views.UpvoteView.as_view(), name="upvote-post")
]
