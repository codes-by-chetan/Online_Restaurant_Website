from django.contrib import admin
from .models import Menu


# Register your models here.

@admin.register(Menu)
class Menu(admin.ModelAdmin):
    list_display = ['id','item_name','item_price']