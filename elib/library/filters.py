import django_filters
from .models import Book, Author, Category, Tags

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = [
            'bookTitle',
            'yearPublished',
            'isbn',
        ]

class AuthorFilter(django_filters.FilterSet):
    class Meta:
        model = Author
        fields = [
            'authorName',
        ]

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = [
            'categoryName',
        ]

class TagsFilter(django_filters.FilterSet):
    class Meta:
        model = Tags
        fields = [
            'tags',
        ]
