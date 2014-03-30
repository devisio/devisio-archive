from django.contrib import admin

from devisio.journals.models import Journal


class JournalAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Journal, JournalAdmin)
