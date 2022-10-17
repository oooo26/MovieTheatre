
from django.contrib import admin
from .models import Author, Movie, Grade

# Register your models here.
admin.site.register(Author)
admin.site.register(Movie)
admin.site.register(Grade)
