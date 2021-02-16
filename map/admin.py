from django.contrib import admin
from django import forms


from .models import VerifiedTag, UnverifiedTag

@admin.register(VerifiedTag)
class VerifiedTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'image', 'location', 'x_coord', 'y_coord', 'user')
    #list_display = ('id', 'name', 'description', 'image', 'location', 'x_coord', 'y_coord', 'image')