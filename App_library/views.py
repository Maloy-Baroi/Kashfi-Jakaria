from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.db.models import Sum
from datetime import date
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic import UpdateView
from App_library.models import *
from App_library.forms import *


# Create your views here.
@login_required
def index(request):
    return render(request, "App_library/Home.html")


@login_required
def categories(request):
    if request.method == "POST":
        title = request.POST.get('title')
        cat = Category(title=title)
        cat.save()
        return HttpResponseRedirect(reverse('App_library:categories'))
    all_categories = Category.objects.all()
    return render(request, "App_library/category.html", context={"categories": all_categories})


@login_required
def delete_category(request, id):
    category = Category.objects.filter(id=id)
    category.delete()
    return HttpResponseRedirect(reverse('App_library:categories'))


@login_required
def edit_category(request, id):
    category = Category.objects.filter(id=id).get()
    if request.method == 'POST':
        cat_title = request.POST.get('title')
        category.title = cat_title
        category.save()
        return HttpResponseRedirect(reverse('App_library:categories'))
    return render(request, 'App_library/edit_category.html', context={'category': category})


def books(request):
    form = AddBookForm()
    bookselfForm = AddNewSelf()
    if request.method == "POST" and 'save_book' in request.POST:
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    elif request.method == "POST" and 'save_bookself' in request.POST:
        bookselfForm = AddNewSelf(request.POST)
        if bookselfForm.is_valid():
            bookselfForm.save()
    all_books = Book.objects.all()
    b = [x for x in all_books]
    if len(b) == 0:
        all_books = None
    all_categories = Category.objects.all()
    return render(request, "App_library/books.html",
                  {"books": all_books, 'b': b, "categories": all_categories, 'form': form, 'bookself': bookselfForm})


def book_edit(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookEditForm(instance=book)
    if request.method == "POST":
        form = BookEditForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_library:books'))
    return render(request, 'App_library/book_edit.html', context={'form': form})


def delete_book(request, id):
    book = Book.objects.filter(id=id).get()
    book.delete()
    return redirect("/books")


def customers(request):
    if request.method == "POST":
        nid = request.POST["nid"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        address = request.POST["address"]
        phone_number = request.POST["phone_number"]
        customer = Customer(NID=nid, firstname=firstname, lastname=lastname, Address=address, phone_number=phone_number)
        customer.save()
        return HttpResponseRedirect(reverse('App_library:customers'))
    all_Customers = Customer.objects.all()
    return render(request, "App_library/Customers.html", context={"Customers": all_Customers})


def borrow(request):
    form = BookBorrowForm()
    b = Borrow.objects.all()
    all_borrower = []
    for i in b:
        if i.status == 'Borrowed':
            borrower = f"{i.customer.firstname} {i.customer.lastname}-{i.customer.NID}"
            all_borrower.append(borrower)
    if request.method == "POST":
        form = BookBorrowForm(request.POST)
        if form.is_valid():
            bro = form.save(commit=False)
            customer = str(f"{bro.customer.firstname} {bro.customer.lastname}-{bro.customer.NID}")
            if customer in all_borrower:
                messages.info(request, "You didn't return your previous book!!!")
            else:
                print("Bad Coding!!!")
                bro.qty = 1
                bro.status = "Borrowed"
                bro.save()
            return HttpResponseRedirect(reverse('App_library:borrow'))
    _customers = Customer.objects.all()
    _books = Book.objects.all()
    datas = []
    for book in _books:
        left = Borrow.objects.filter(status="Borrowed", book__title=book.title).aggregate(Sum('qty'))
        if left['qty__sum'] is None:
            l = 0
        else:
            l = int(left['qty__sum'])
        datas.append(book.available - l)
    all_datum = zip(_books, datas)
    return render(request, "App_library/borrow.html", {"datas": all_datum, "customers": _customers, 'form': form})


def returning(request):
    if request.method == "POST":
        b_id = int(request.POST["borrow_id"])
        _borrow = Borrow.objects.get(id=b_id)
        _borrow.date = datetime.now()
        _borrow.status = "Returned"
        _borrow.save()
        return HttpResponseRedirect(reverse('App_library:returning'))
    borrows = Borrow.objects.all()
    return render(request, "App_library/return.html", {"borrows": borrows})
