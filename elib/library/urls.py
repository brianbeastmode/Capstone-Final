from django.urls import path
from . import views


urlpatterns = [
    path('login', views.login, name= 'login'),
    path('', views.index, name = 'index'),
    path('library/', views.library, name = 'library'),
    path('library/add/', views.createBook, name = 'create_book'),
    path('library/update/<int:id>', views.updateBook, name = 'update_book'),
    path('library/delete/<int:id>', views.deleteBook, name = 'delete_book'),
    path('library/add-author/', views.addAuthor, name = 'add_author'),
    path('staff/', views.staff, name = 'staff'),
    path('services/', views.services, name = 'services'),
    path('about/', views.about, name = 'about'),
    # path('library/<slug:authorName>', views.authorSearch, name='author_search'),
    path('library/<int:id>/<slug:bookTitle>/', views.book, name = 'book_preview'),
    path('library/<int:id>', views.reviewBook, name = 'review'),
    path('library/<int:id>/<str:bookTitle>/bookrender', views.bookRender, name = 'render_book'),
    path('web/viewer.html', views.pdf_view, name="pdf_viewer"), 
]
