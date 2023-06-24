"""
URL configuration for bibliotecaApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from books import views as book_views
from users import views as users_views

urlpatterns = [
    path("", book_views.index),
    path("home", book_views.index),
    path('books/', book_views.all, name="books"),
    path('books/book/', book_views.book, name="books"),
    path('books/materia/', book_views.materia, name="books"),
    path('books/autor/', book_views.autor, name="books"),
    path('books/prestado/', book_views.prestado, name="books"),
    #path("books/", include("books.urls")),
    path('users/sancionados/', users_views.index, name="users"),
    path('admin/', admin.site.urls),
]
