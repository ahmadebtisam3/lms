from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import BookIssued


# Register your models here.
class BookIssuedAdmin(ModelAdmin):
    list_display: list[str] = [
        "book_issue",
        "issued_to",
        "issued_date",
        "returning_date",
        "available"
    ]
    search_fields = [
        "issued_date",
        "returning_date",
        "returned_at",
        "issued_to",
        "book_issue"
    ]

    def available(self, obj):
        return bool(obj.returned_at)

    available.short_description = "Book available"
    available.boolean = True


admin.site.register(
    BookIssued,
    BookIssuedAdmin)
