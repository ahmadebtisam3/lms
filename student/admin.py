from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from .models import Student


# Register your models here.
class StudentAdmin(ModelAdmin):
    list_display: list[str] = [
        "role_number",
        "name",
        "address",
    ]
    search_fields = [
        "role_number",
        "name",
        "address",
    ]


admin.site.register(
    Student,
    StudentAdmin)
