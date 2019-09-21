from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .forms import CommentForm
from .models import Comment, Post


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    context_object_name = 'latest_posts'

    def get_queryset(self):
        # returns the most recent blog posts
        return Post.objects.order_by('-pub_date')


class PostView(generic.UpdateView):
    model = Post
    template_name = 'blog/post.html'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['comments'] = self.get_object().get_comments()
        context['form'] = CommentForm
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        post = self.get_object()
        if form.is_valid():
            Comment.objects.create(**form.cleaned_data, post=post, pub_date=datetime.now())
            return HttpResponseRedirect(reverse('blog:post', kwargs={'pk': post.id}))
        context = {
            'post': post,
            'comments': post.get_comments(),
            'form': form
        }
        return render(request, self.template_name, context)
