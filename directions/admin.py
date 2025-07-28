from django.contrib import admin
from django.utils.html import format_html
from parler.admin import TranslatableAdmin

from . import models

@admin.register(models.Companies)
class CompaniesAdmin(TranslatableAdmin):  # Исправлено: должно быть admin.ModelAdmin
    list_display = ('preview', 'title', 'created_at', 'link')
    list_display_links = ('preview', 'title', 'link')
    readonly_fields = ('preview', 'created_at')  # Добавлено preview в readonly
    ordering = ('-created_at',)
    list_per_page = 20  # Добавлено для пагинации
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'fields': ('image', 'title', 'text', 'link')
        }),
        ('Дополнительно', {
            'fields': ('preview', 'created_at'),  # Добавлено preview
            'classes': ('collapse',)
        }),
    )

    @admin.display(description="Превью")
    def preview(self, obj):
        if obj.image and hasattr(obj.image, 'url'):  # Добавлена проверка на наличие url
            return format_html(
                '<img src="{}" style="max-height: 100px; max-width: 150px; '
                'object-fit: contain; border: 1px solid #ddd; border-radius: 4px;"/>',
                obj.image.url
            )
        return "Нет изображения"  # Добавлен fallback

