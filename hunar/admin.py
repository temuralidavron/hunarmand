from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Anketa, User, MarkAnketa


class Markanketainline(admin.TabularInline):
    model = MarkAnketa


#
# class Users(admin.UserAdmin):
#     list_display = ['username', 'login']
admin.site.register(Anketa)
admin.site.register(User,UserAdmin)

# fields = list(UserAdmin.fieldsets)
# fields[1]=('Personal Info',{'fields':('first_name')})
# # UserAdmin.fieldsets=tuple(fields)




