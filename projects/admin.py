from django.contrib import admin
from django.utils.html import format_html
from parler.admin import TranslatableAdmin

from . import models


@admin.register(models.Projects)
class ProjectsAdmin(TranslatableAdmin):
    list_display = ('preview', 'title', 'location', 'is_finish', 'slug',)
    list_display_links = ('preview', 'title', 'location')
    readonly_fields = ('preview', 'created_at', )
    list_per_page = 20
    search_fields = ('translations__title', )
    list_filter = ('is_finish', 'is_featured')

    fieldsets = (
        (None, {
            'fields': ('image', 'title', 'location', 'text', 'is_finish', 'is_featured', 'slug')
        }),
        ('Дополнительно', {
            'fields': ('preview', 'created_at',),
            'classes': ('collapse',)
        }),
    )

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)} 

    @admin.display(description='Превью')
    def preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 150px; '
                'object-fit: contain; border: 1px solid #ddd; border-radius: 4px;"/>',
                obj.image.url
            )
        return "Нет изображения"