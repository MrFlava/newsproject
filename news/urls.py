from django.urls import path
from news import views

app_name = "news"

urlpatterns = [
    path("create", views.PostCreateView.as_view(), name="add-post"),
    path("update-post/<int:pk>", views.PostUpdateView.as_view(), name="update-post"),
    path("delete-post/<int:pk>", views.PostDeleteView.as_view(), name="delete-post"),
    path("show-posts", views.PostsListView.as_view(), name="show-posts"),

]
