from django.contrib import admin
from .models import RegistersModel,CreateTaskModel
from django.contrib.auth.admin import UserAdmin

# from .forms import CustomCreationForm,CustomUserChangeForm

class Registeradmin(admin.ModelAdmin):
    list_display = ['name','email','password']
admin.site.register(RegistersModel,Registeradmin)

class CreateTaskAdmin(admin.ModelAdmin):
    list_display = ['tittle','status']
admin.site.register(CreateTaskModel,CreateTaskAdmin)


#
# class CustomUserAdmin(UserAdmin):
#     add_form=CustomCreationForm
#     form=CustomUserChangeForm
#     model=RegistersModel
#     list_display= ['email','password']
# admin.site.register(RegistersModel,CustomUserAdmin)

