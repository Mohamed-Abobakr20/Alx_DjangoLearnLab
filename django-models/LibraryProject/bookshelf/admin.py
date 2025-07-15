from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # display these fields in the list view
    list_filter = ('publication_year',)                     # add filter by publication year
    search_fields = ('title', 'author')     

admin.site.register(Book, BookAdmin)
   
