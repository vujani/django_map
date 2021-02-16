from django.contrib import admin
from django import forms


from .models import UnverifiedTag, Tag

@admin.register(UnverifiedTag)
class UnverifiedTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'location', 'x_coord', 'y_coord', 'username', 'email')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'location', 'x_coord', 'y_coord', 'user')
