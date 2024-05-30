# api_produccion/admin.py

from django.contrib import admin
from .models import Content, Actor, Director, Genre

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'poster_url', 'trailer_url', 'duration_minutes', 'num_episodes')
    search_fields = ('title',)
    list_filter = ('type',)
    fieldsets = (
        (None, {
            'fields': ('type', 'title', 'poster_url', 'trailer_url')
        }),
        ('Details', {
            'fields': ('duration_minutes', 'num_episodes'),
            'classes': ('collapse',)
        }),
        ('Associations', {
            'fields': ('actors', 'directors', 'genres'),  # Aquí se utilizan los nombres correctos
        }),
    )
    filter_horizontal = ('actors', 'directors', 'genres')  # Utiliza los nombres correctos de los campos

admin.site.register(Content, ContentAdmin)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Genre)
