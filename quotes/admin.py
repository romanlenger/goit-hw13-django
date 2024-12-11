from django.contrib import admin

# Register your models here.
from .models import Tag, Author, Quote

# Register your models here.
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Quote)