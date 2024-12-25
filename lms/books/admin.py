from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Book


# Register your models here.

class BookAdmin(ModelAdmin):
    list_display: list[str] = [
        "number",
        "name",
        "topic",
        "price",
    ]
    search_fields = [
        "number",
        "name",
        "topic",
        "price",
        "description"
    ]


admin.site.register(
    Book,
    BookAdmin)
