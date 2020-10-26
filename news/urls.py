from django.urls import path
from news import views

app_name = "news"

urlpatterns = [
    path("create", views.PostCreateView.as_view(), name="add-post"),
    path("show-posts", views.PostsListView.as_view(), name="show-posts"),
]