from django.contrib import admin

from devisio.journals.models import Journal, JournalSection


class JournalSectionInline(admin.TabularInline):
    model = JournalSection
    extra = 1
    prepopulated_fields = {'slug': ('headline',)}


class JournalAdmin(admin.ModelAdmin):
    inlines = [JournalSectionInline]
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Journal, JournalAdmin)
