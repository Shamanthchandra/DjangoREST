from django.contrib import admin
from loginpage.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','fullname','email_id']

admin.site.register(User, UserAdmin)