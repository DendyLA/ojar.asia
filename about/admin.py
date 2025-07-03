from django.contrib import admin
from django.utils.html import format_html
from django.contrib import admin

from . import models

@admin.register(models.AboutMain)
class VideosAdmin( admin.ModelAdmin):
    list_display = ( 'title', 'text',)
    list_display_links = ('title', 'text' )
    readonly_fields = ('created_at', )

    list_per_page = 20  # Добавлено для пагинации
    search_fields = ('title',)
    
    fieldsets =(
        (None, {
            'fields' : ('title', 'text','video')
        }),
        ('Дополнительно', {
            'fields' : ( 'created_at', ),
            'classes' : ('collapse',)
        }),
    )


@admin.register(models.Info)
class InfoAdmin( admin.ModelAdmin):
    list_display = ( 'category', 'number',)
    list_display_links = ('category', 'number', )
    readonly_fields = ('created_at', )

    list_per_page = 20  # Добавлено для пагинации
    search_fields = ('category',)
    
    fieldsets =(
        (None, {
            'fields' : ('category', 'number',)
        }),
        ('Дополнительно', {
            'fields' : ( 'created_at', ),
            'classes' : ('collapse',)
        }),
    )


@admin.register(models.Comment)
class CommentAdmin( admin.ModelAdmin):
    list_display = ('preview', 'author', 'position')
    list_display_links = ('preview', 'author', 'position')
    readonly_fields = ('preview',)

    list_per_page = 20  # Добавлено для пагинации
    search_fields = ('author',)
    
    fieldsets =(
        (None, {
            'fields' : ('image', 'author','position' , 'text')
        }),
        ('Дополнительно', {
            'fields' : ('preview', ),
            'classes' : ('collapse',)
        }),
    )

    @admin.display(description='Превью')
    def preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 150px; '
                'object-fit: contain; border: 1px solid #ddd; border-radius: 4px;"/>',
                obj.image.url
            )
        return "Нет изображения"