from django.contrib import admin
from .models import User1,User2
from .models import Test
from django.contrib.auth.admin import UserAdmin
class TestAdmin(admin.ModelAdmin):
	list_display = ['number','sections','question', 'A', 'B', 'C','answer',]
admin.site.register(Test, TestAdmin)

class User1Admin(admin.ModelAdmin):
    list_display = ['user','first_name','last_name',]
admin.site.register(User1, User1Admin)


class User2Admin(admin.ModelAdmin):
    list_display = ['user','email','university', 'speciality','checking','score',]
admin.site.register(User2, User2Admin)
