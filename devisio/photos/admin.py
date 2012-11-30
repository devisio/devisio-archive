from django.contrib import admin
from django.contrib.auth import get_user_model

from models import Album


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'visible')
    prepopulated_fields = {'slug': ('name',)}

    def save_model(self, request, obj, form, change):
        try:
            obj.owner
        except get_user_model().DoesNotExist:
            obj.owner = request.user
        obj.save()

admin.site.register(Album, AlbumAdmin)
