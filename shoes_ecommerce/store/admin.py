from django.contrib import admin
from .models import Shoes

@admin.register(Shoes)
class ShoeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')  # Display these fields in the admin list view
    search_fields = ('name',)  # Add a search bar to search by name

