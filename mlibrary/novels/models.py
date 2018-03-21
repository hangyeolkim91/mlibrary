from django.db import models
from django.utils import timezone

# Create your models here.

class Bookcase(models.Model):
    name = models.CharField(max_length=500)

class Novel(models.Model):
    bookcase= models.ForeignKey(Bookcase, on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateField()
    file = models.FileField(upload_to='uploads/',max_length=500, null=True)

    def __str__(self):
        return self.title
