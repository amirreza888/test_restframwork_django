from django.contrib import admin
from .models import Book
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fields = ['title','description']
    list_display = ['title','price']
    list_filter = ['title']