from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUserRegistration
from .forms import CustomUserRegistrationForm, CustomUserChangeForm
# Register your models here.
class ShowAdminPage(UserAdmin):
    list_display = ['username', 'email', 'is_staff', 'is_superuser']
    form = CustomUserChangeForm
    model = CustomUserRegistration
    add_form = CustomUserRegistrationForm
    readonly_fields = ('last_login', 'date_joined')

    fieldsets = (
        (None, {'fields':('username','password',)}),
        ('Personal info', {'fields':('first_name','last_name','email',)}),
        ('Permissions', {'fields':('is_staff','is_active','is_superuser','groups','user_permissions')}),
        ('Important dates', {'fields':('last_login','date_joined')}),
    )
    add_fieldsets = (
        (None,{
            'classes':('wide',),
            'fields':('username','password1','password2'),
        }),
    )

admin.site.register(CustomUserRegistration, ShowAdminPage)