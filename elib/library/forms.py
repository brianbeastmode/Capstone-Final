from django.forms import ModelForm
from .models import Book, Review, Author

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__' 

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'rating']

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['authorName']