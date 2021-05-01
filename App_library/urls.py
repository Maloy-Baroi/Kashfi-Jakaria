from django.conf.urls import url, include
from django.urls import path

from . import views

app_name = 'App_library'

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^books$', views.books, name="books"),
    url(r'^categories$', views.categories, name="categories"),
    url(r'^customers$', views.customers, name="customers"),
    url(r'^returning$', views.returning, name="returning"),
    url(r'^borrow$', views.borrow, name="borrow"),
    path('edit_book/<int:pk>', views.book_edit, name="edit_book"),
    url(r'^edit_category/(\d+)/$', views.edit_category, name="edit_category"),
    url(r'^delete_book/(\d+)/$', views.delete_book, name="delete_book"),
    url(r'^delete_category/(\d+)/$', views.delete_category, name="delete_category"),
]
