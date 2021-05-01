from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


# Create your models here.
class EmployeeID(models.Model):
    ids = models.CharField(max_length=20)


class User(AbstractUser):
    phone_regex = RegexValidator(regex=r"^\+?(88)01[3-9][0-9]{8}$", message=_(
        "Enter a valid Bangladesh mobile phone number starting with +(country code)"))
    phone_number = models.CharField(validators=[phone_regex], verbose_name=_("Mobile phone"), max_length=17,
                                    blank=False, null=True)
    employee_id = models.CharField(max_length=20, unique=True)
    profile_picture = models.ImageField(upload_to='librarian_photo')
