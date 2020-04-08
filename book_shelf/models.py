from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid




class Author(models.Model):
    author_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    author_name = models.CharField(max_length=200)
    author_description = models.CharField(max_length=500)
    def add_author(self):
        #self.published_date = timezone.now()
        self.save()


class Book(models.Model):
    book_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book_title = models.CharField(max_length=100)
    book_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    year = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=100, null=True, blank=True)
    lable = models.CharField(max_length=50, null=True, blank=True)
    read_status = models.IntegerField(default=1)
    who_has = models.CharField(max_length=50, default="YOU", editable=True)
    who_ownes = models.CharField(max_length=50, default="YOU", editable=True)
    e_book = models.FileField(null=True, blank=True)
    priority = models.IntegerField(default=0)
    created_date = models.DateField(auto_now_add=True,)

    def change_status_to_in_progress(self):
        self.read_status = "2"
        self.save()
    def change_status_to_done(self):
        self.read_status = "3"
        self.save()

    def add_book(self):
        #self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return "'" + self.book_title + "'" + " by " + self.book_author.author_name + ";"




