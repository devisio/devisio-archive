from django.contrib import admin
from django.contrib.auth import get_user_model

from devisio.photos.models import Album, Photo


class PhotoAdminInline(admin.TabularInline):
    model = Photo
    extra = 0


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'visible', 'photos')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [PhotoAdminInline]

    def photos(self, obj):
        return '<ul class="grp-actions"><li class="grp-change-link"><a href="/admin/filebrowser/upload/?&dir='+obj.get_path()+'" class="">Add photos</a></li></ul>'
    photos.allow_tags = True

    def save_model(self, request, obj, form, change):
        try:
            obj.owner
        except get_user_model().DoesNotExist:
            obj.owner = request.user
        obj.save()

admin.site.register(Album, AlbumAdmin)
