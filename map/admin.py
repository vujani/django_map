from django.contrib import admin
from django import forms


from .models import UnverifiedTag, Tag, Images, UImages

@admin.register(UnverifiedTag)
class UnverifiedTagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'location', 'x_coord', 'y_coord', 'username', 'email')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'location', 'x_coord', 'y_coord', 'user')


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')


@admin.register(UImages)
class UImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')
