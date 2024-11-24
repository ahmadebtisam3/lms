from django.db import models
from books.models import Book
from student.models import Student


# Create your models here.
class BookIssued(models.Model):
    issued_date = models.DateTimeField(auto_now_add=True)
    returning_date = models.DateTimeField()
    returned_at = models.DateTimeField()
    issued_to = models.ForeignKey(
        to=Student, on_delete=models.SET_NULL,
        related_name="books_issues",
        null=True
    )
    book_issue = models.ForeignKey(
        to=Book, on_delete=models.SET_NULL,
        related_name="issues",
        null=True
    )

    def __str__(self):
        return "{} ({})".format(self.book_issue, self.returning_date)
