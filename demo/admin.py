from django.contrib import admin
from .models import Book, BookNumber, Character,Author
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    #fields = ['title','description']
    list_display = ['title','price']
    list_filter = ['title']


admin.site.register(BookNumber)
admin.site.register(Character)
admin.site.register(Author)