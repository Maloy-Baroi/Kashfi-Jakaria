from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.db import models
from datetime import date


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.title}"


class BookLocation(models.Model):
    self_no = models.CharField(max_length=255)
    row_no = models.CharField(max_length=255)

    def __str__(self):
        return f"Self-{self.self_no}, Row-{self.row_no}"


class Book(models.Model):
    title = models.CharField(max_length=255, unique=True)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='book_cover')
    author = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=25000, blank=True, null=True)
    available = models.PositiveIntegerField(default=0)
    location = models.ForeignKey(BookLocation, on_delete=models.CASCADE, related_name='book_location')

    def __str__(self):
        return f"'{self.title}' by '{self.author}'"


class Customer(models.Model):
    NID = models.CharField(max_length=255, unique=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    phone_regex = RegexValidator(regex=r"^\+?(88)01[3-9][0-9]{8}$", message=_(
        "Enter a valid Bangladesh mobile phone number starting with +(country code)"))
    phone_number = models.CharField(validators=[phone_regex], verbose_name=_("Mobile phone"), max_length=17,
                                    blank=False, null=True)
    year = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}-{self.NID}"


class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    qty = models.IntegerField(default=0)
    date = models.DateField(default=date.today)
    status = models.CharField(max_length=25)
