from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)  # ToDo: Create Author model
    pub_date = models.DateTimeField('date published')
    content = models.TextField()

    def __str__(self):
        return f'"{self.title}" by {self.author} - {self.pub_date.strftime("%B %d, %Y")}'
