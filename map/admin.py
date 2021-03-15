from django.contrib import admin
from .models import UnverifiedTag, Tag


# fogstream12345 - пароль от пользователей
# admin - admin

@admin.register(UnverifiedTag)
class UnverifiedTagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'image',
        'location',
        'x_coord',
        'y_coord',
        'username',
        'email'
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'description',
        'image',
        'location',
        'x_coord',
        'y_coord',
        'user'
    )
