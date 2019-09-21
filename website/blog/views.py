from django.views import generic

from .models import Post


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
