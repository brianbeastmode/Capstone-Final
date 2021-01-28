from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Author(models.Model):
    authorName = models.CharField(max_length=30)

    def __str__(self):
        return self.authorName

class Category(models.Model):
    categoryName = models.CharField(max_length=20)

    def __str__(self):
        return self.categoryName
        
class Tags(models.Model):
    tags = models.CharField(max_length=20)

    def __str__(self):
        return self.tags

class Book(models.Model):
    bookTitle = models.CharField(max_length=100)
    bookAuthor = models.ManyToManyField(Author)
    bookDescription = models.TextField()
    bookCategory = models.ManyToManyField(Category)
    bookTags = models.ManyToManyField(Tags)
    yearPublished = models.IntegerField(validators=[MaxValueValidator(9999)])
    bookFile = models.FileField(upload_to='books', null=True, blank=True)
    bookImage = models.ImageField(upload_to='covers', blank=True)
    isbn = models.IntegerField(blank=True)
    pages = models.IntegerField(validators=[MaxValueValidator(10000), MinValueValidator(0)])
    featured = models.BooleanField()

    def __str__(self):
        return self.bookTitle

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=500)
    rating = models.FloatField(default=0,validators=[MaxValueValidator(10), MinValueValidator(0)] )

    def __str__(self):
        return self.user.username


