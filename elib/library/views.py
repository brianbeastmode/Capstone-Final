from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.db.models import Q
from .models import Book, Author, Category, Tags, Review
from .forms import BookForm, ReviewForm, AuthorForm
from .filters import BookFilter, AuthorFilter
from .decorators import unauthenticated_user, authenticated_user

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.clickjacking import xframe_options_exempt



# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from django.http import HttpResponse, FileResponse, Http404, HttpResponseNotFound



def is_query_valid(param):
    return param != '' and param is not None

@authenticated_user
def login(request): 
    return render(request, "login.html")

@unauthenticated_user
def index(request):
    qs = Book.objects.all()
    qs = qs.filter(featured=True)
            
    context = {
        'books': qs
        }
        
    return render(request, "html/index.html", context)

def library(request): #filter and display books
    qs = Book.objects.all().order_by('bookTitle')
    context = {}

    if request.user.is_authenticated:
        all_query = request.GET.get('all_query')
        title_author_query = request.GET.get('title_author')
        category_query = request.GET.get('category')
        isbn_query = request.GET.get('isbn')
        min_year_query = request.GET.get('min_year')
        max_year_query = request.GET.get('max_year')
        file_available_query = request.GET.get('file_available')
        file_unavailable_query = request.GET.get('file_unavailable')
        
        
        if is_query_valid(all_query):
            qs = qs.filter(Q(bookTitle__icontains=all_query) | Q(bookAuthor__authorName__icontains=all_query)
            | Q(bookCategory__icontains=all_query) | Q(isbn__iexact=all_query) | Q(yearPublished__iexact=all_query)).distinct()
            
        if is_query_valid(title_author_query):
            qs = qs.filter(Q(bookTitle__icontains=title_author_query) | Q(bookAuthor__authorName__icontains=title_author_query)).distinct()

        if is_query_valid(category_query):
            qs = qs.filter(bookCategory__icontains=category_query)
        
        if is_query_valid(isbn_query):
            qs = qs.filter(isbn__iexact=isbn_query)

        if is_query_valid(min_year_query):
            qs = qs.filter(yearPublished__gte=min_year_query)

        if is_query_valid(max_year_query):
            qs = qs.filter(yearPublished__lte=max_year_query)

        if file_available_query =='on' :
            qs = qs.filter(bookFile__istartswith='books')
        
        if file_unavailable_query =='on':
            qs = qs.filter(bookFile='')

        context['books'] = qs

        paginator = Paginator(qs, 9)
        page = request.GET.get('page', 1)

        try:
            response = paginator.page(page)
        except PageNotAnInteger:
            response = paginator.page(1)
        except EmptyPage:
            response = paginator.page(paginator.num_pages)

        context['paginated'] = response

        return render(request, "library.html", context)
    else:
        return render(request, "login.html")


# def authorSearch(request, authorName): #search for all same author queries
#     qs = Author.objects.filter(authorName=authorName)
#     book = Book.objects.all()

#     if request.user.is_authenticated:
#         author_query = qs
    
#         if is_query_valid(author_query): #if author is not none or blank filter all books with this author
#             qs = qs.filter(authorName__iexact=author_query)
            
#         context = {
#             'queryset': qs,
#             'book': book
#         }
#         print(qs)
#         return render(request, "library.html", context)
#     else:
#         return render(request, "login.html")

# def authorSearch(request, authorName): #search for all same author queries
#     author = Author.objects.get(authorName=authorName)
#     book = Book.objects.filter(bookAuthor=author)
#     context = {
#         # 'queryset': qs,
#         'book': book
#     }
#     return render(request, "library.html", context)

def book(request, bookTitle, id):
    book = Book.objects.get(bookTitle=bookTitle.replace('-',' '))
    author = Author.objects.all()
    review = Review.objects.filter(book=id)
    # review = Review.objects.filter(book=id)
    context = {
        'book': book,
        'author': author,
        'review': review
    }
    if request.user.is_authenticated:
        return render(request, "book.html", context)
    else:
        return render(request, "login.html")

def reviewBook(request, id):
    book = Book.objects.get(id=id)
    
    if request.method == "POST":
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            data = form.save(commit=False)
            data.comment = request.POST["comment"]
            data.rating = request.POST["rating"]
            data.user = request.user
            data.book = book
            data.save()

            return redirect("book_preview", book.id, book.bookTitle.replace(' ', '-'))
        else:
            return redirect("book_preview", book.id, book.bookTitle.replace(' ', '-'))

    else:
        form = ReviewForm()

    

def createBook(request):
    form = BookForm()

    if request.method == "POST":
        form = BookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

            return redirect("create_book")




    context = {
        'form': form
    }

    return render(request, "test.html", context)

def updateBook(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(instance=book)

    if request.method == "POST":
        form = BookForm(request.POST or None, request.FILES or None, instance=book)
        if form.is_valid():
            form.save()

            return redirect("library")


    context = {
        'form': form
    }

    return render(request, "add.html", context)

def deleteBook(request, id):
    book = Book.objects.get(id=id)
    if request.method == "POST":
        book.delete()
        return redirect("library")

    
    context = {
        'book': book
    }
    return render(request, "delete.html", context)

def addAuthor(request):
    form = AuthorForm()

    if request.method == "POST":
        print(request.POST)
        form = AuthorForm(request.POST or None)
        if form.is_valid():
            print(form)
            form.save()

            return redirect("add_author")


    context = {
        'form': form
    }

    return render(request, "add-author.html", context)

def staff(request):
    if request.user.is_authenticated:
        return render(request, "staff.html")
    else:
        return render(request, "login.html")

def services(request):
    if request.user.is_authenticated:
        return render(request, "services.html")
    else:
        return render(request, "login.html")

def about(request):
    if request.user.is_authenticated:
        return render(request, "about.html")
    else:
        return render(request, "login.html")

@xframe_options_exempt
def bookRender(request, id, bookTitle):
    book = Book.objects.get(id=id, bookTitle=bookTitle)
    if request.user.is_authenticated:
        return render(request, 'book-render.html', {'books':book})
    else:
        return render(request, "login.html")

def pdf_view(request):
    return render(request, 'viewer.html')

# def userManual(request, id, title):
#     book = Books.objects.get(id=id, bookTitle=title)
#     file_location = './media/books/Queueing.v3.pdf'

#     try:    
#         with open(file_location, 'r') as f:
#            file_data = f.read()

#         # sending response 
#         response = HttpResponse(file_data, content_type='application/pdf')
#         # response['Content-Disposition'] = ' filename="report.pdf"'

#     except IOError:
#         # handle file not exist case here
#         response = HttpResponseNotFound('<h1>File not exist</h1>')

#     return response

