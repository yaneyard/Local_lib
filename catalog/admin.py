from .models import Author, Genre, Book, BookInstance, Language
from django.contrib import admin

class BooksInstanceInLine(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInLine]

class BooksInLine(admin.TabularInline):
    model = Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInLine]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('id', 'book', 'status', 'due_back', 'imprint')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Abailability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


admin.site.register(Language)
admin.site.register(Genre)