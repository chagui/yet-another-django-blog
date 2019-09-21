from django.contrib import admin

from .models import Comment, Post


class PostAdmin(admin.ModelAdmin):
    fields = ('title', 'pub_date', 'content')

    def get_queryset(self, request):
        queryset = super(PostAdmin, self).get_queryset(request)
        return queryset if request.user.is_superuser else queryset.filter(author=request.user)

    def save_model(self, request, post, form, change):
        post.author = request.user
        super(PostAdmin, self).save_model(request, post, form, change)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
