from django.contrib import admin
from django.contrib.auth import get_user_model

from devisio.journals.models import Journal, JournalEntry


class JournalEntryInline(admin.TabularInline):
    model = JournalEntry
    extra = 0


class JournalAdmin(admin.ModelAdmin):
    inlines = [JournalEntryInline]

    def save_model(self, request, obj, form, change):
        try:
            obj.owner
        except get_user_model().DoesNotExist:
            obj.owner = request.user
        obj.save()

admin.site.register(Journal, JournalAdmin)
admin.site.register(JournalEntry)
