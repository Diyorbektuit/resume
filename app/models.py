from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=123)
    description = models.TextField(max_length=10000)
    link = models.CharField(max_length=123)
    github_link = models.CharField(max_length=123)
    img = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=100)

    def __str__(self):
        return self.name