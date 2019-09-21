from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        # returns the most recent blog posts
        return Post.objects.order_by('-pub_date')


class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'
