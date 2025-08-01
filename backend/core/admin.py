from django.contrib import admin
from .models import Entry, Project  # import your models

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'address', 'image')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Register your models here.

