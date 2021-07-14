from django.contrib import admin
from .models import Room, Car, Student

# # added with user creation
# from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin, UserChangeForm
# from .models import User


# Register your models here.
admin.site.register(Room)
admin.site.register(Car)
admin.site.register(Student)


# #added with user creation
# class UserAdmin(BaseUserAdmin):
#     form = UserChangeForm
#     fieldsets = (
#         (None, {'fields': ('email', 'password',)}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#         (_('user_info'), {'fields': ('native_name',)}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide', ),
#             'fields': ('email', 'password1', 'password2'),
#         }),
#     )
#     list_display = ['email', 'first_name', 'last_name', 'is_staff', "native_name"]
#     search_fields = ('email', 'first_name', 'last_name')
#     ordering = ('email', )

# admin.site.register(User, UserAdmin)


