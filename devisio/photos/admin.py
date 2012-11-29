from django.contrib import admin

from models import Album


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')

admin.site.register(Album, AlbumAdmin)
