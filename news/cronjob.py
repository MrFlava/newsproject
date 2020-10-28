from .models import Post


def reset_upvotes_count():
    posts = Post.objects.all()
    for p in posts:
        p.upvotes_amount = 0
        p.save()
