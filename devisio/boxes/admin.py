from django.contrib import admin

from devisio.boxes.models import Box, Photo


class BoxAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Box, BoxAdmin)
admin.site.register(Photo)
