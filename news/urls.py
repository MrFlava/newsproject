from django.urls import path
from news import views

app_name = "news"

urlpatterns = [
    path("posts/create", views.PostCreateView.as_view(), name="create-post"),
    path("posts/<int:pk>/update", views.PostUpdateView.as_view(), name="update-post"),
    path("posts/<int:pk>/delete", views.PostDeleteView.as_view(), name="delete-post"),
    path("posts/upvote", views.UpvoteView.as_view(), name="upvote-post"),
    path("posts", views.PostsListView.as_view(), name="show-posts"),
    path("comments/create", views.CommentCreateView.as_view(), name="create-comment"),
    path("comments", views.CommentListView.as_view(), name="show-comments"),

]
