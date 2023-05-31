from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Categorie)
@admin.register(Wood)
class WoodAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')
    list_filter = ('date', 'title', 'category')
    search_fields = ('title', 'category')
    date_hierarchy = 'date'

admin.site.register(Newsletter)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')
    list_filter = ('date', 'email', 'name')
    search_fields = ('name', 'message')
    date_hierarchy = 'date'