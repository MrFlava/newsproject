from django.contrib import admin
from news.models import Post, Comment, Upvote

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    model = Post


class CommentAdmin(admin.ModelAdmin):
    model = Comment


class UpvoteAdmin(admin.ModelAdmin):
    model = Upvote


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Upvote, UpvoteAdmin)