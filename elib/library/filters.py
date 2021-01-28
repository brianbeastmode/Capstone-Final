import django_filters
from .models import Book, Author

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = [
            'bookTitle',
            'yearPublished',
            'isbn',
            'bookAuthor',
        ]
class AuthorFilter(django_filters.FilterSet):
    class Meta:
        model = Author
        fields = [
            'authorName',
        ]