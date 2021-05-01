from django.contrib import admin
from App_login.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ['pk', 'email', 'username', 'first_name', 'last_name']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': 'teacher_id'}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': 'teacher_id'}),
    )


admin.site.register(User, UserAdmin)
admin.site.register(EmployeeID)
