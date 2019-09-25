from django.contrib import admin

from .models import PostStatus
from .models import Comment, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = ('title', 'pub_date', 'content', 'status')

    def get_queryset(self, request):
        queryset = super(PostAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(author=request.user).exclude(status=PostStatus.DELETED.value)

    def save_model(self, request, post, form, change):
        post.author = request.user
        super(PostAdmin, self).save_model(request, post, form, change)

    def delete_model(self, request, post):
        if request.user.is_superuser:
            super().delete_model(request, post)
        post.status = PostStatus.DELETED.value
        post.save()


class CommentAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'Deleted')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
