from django.contrib import admin
from App_library.models import *

# Register your models here.
admin.site.register(Customer)
admin.site.register(Book)
admin.site.register(Borrow)
admin.site.register(Category)
admin.site.register(BookLocation)
