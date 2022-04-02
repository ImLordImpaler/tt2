from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Comment(models.Model):
    body = models.CharField(max_length=10000)
    article = models.ForeignKey('Article', on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True , blank=True , null=True)
    def __str__(self):
        return self.body
class Article(models.Model):
    heading = models.CharField(max_length=1000)
    slug = models.CharField(max_length=1000 , null=True , blank=True)
    created_on = models.DateField(auto_now_add=True)
    text = models.TextField()
    tags = models.ManyToManyField(Tag , blank=True)
    comments = models.ManyToManyField(Comment , blank=True, related_name='article_comments')
    def __str__(self):
        return self.heading