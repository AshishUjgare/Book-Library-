from django.contrib import admin
from sixth_app.models import BOOK

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['bid' , 'bname' , 'bauthor' , 'bprice']
admin.site.register(BOOK, BookAdmin)
