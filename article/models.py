from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Article(models.Model):
    heading = models.CharField(max_length=1000)
    slug = models.CharField(max_length=1000 , null=True , blank=True)
    created_on = models.DateField(auto_now_add=True)
    text = models.TextField()
    tags = models.ManyToManyField(Tag , blank=True)

    def __str__(self):
        return self.heading