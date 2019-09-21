from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    pub_date = models.DateTimeField('date published')
    content = models.TextField()

    def get_comments(self):
        return Comment.objects.filter(post=self)

    def number_of_comments(self):
        return self.get_comments().count()

    def __str__(self):
        return f'"{self.title}" by {self.author} - {self.pub_date.strftime("%B %d, %Y")}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    pub_date = models.DateTimeField('date published')
    content = models.TextField()

    def __str__(self):
        return f'{self.name} comment on {self.post.title}'
