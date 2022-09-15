from django.db import models
import os

def cover_rename(Book, cover_name):
    cover_type = cover_name.split('.')[-1]
    new_cover_name = '{}.{}'.format(Book.name, cover_type)
    return os.path.join('cover/', new_cover_name)

class Book(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    translator = models.CharField(max_length=150, null= True)
    year = models.IntegerField(4)
    genre = models.CharField(max_length=150)
    summary = models.TextField(max_length=800)
    cover = models.ImageField(upload_to  = cover_rename)


class Comment(models.Model):
    comment = models.TextField(max_length=800)
    book = models.ForeignKey('book',on_delete=models.CASCADE)
    user = models.ForeignKey('account.User',on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True, blank=True)