from django.contrib import admin
from adminsortable2.admin import SortableAdminMixin, SortableInlineAdminMixin

# Register your models here.

from django.utils.safestring import mark_safe

from .forms import AlbumAdminForm
from .models import *


@admin.register(Preview_Video)
class PreviewVideoAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')
    pass


@admin.register(Work)
class WorkAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('number', 'name', 'choice_player')
    pass


@admin.register(Video)
class VideoAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('number', 'name', 'choice_player', 'director')
    pass


class VideoInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Video
    extra = 0


@admin.register(Director)
class DirectorAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('number', 'name', 'preview_img')
    readonly_fields = ["preview_img"]

    def preview_img(self, obj):
        return mark_safe(f'<img src="{obj.preview_url}" height="200">')
    inlines = [VideoInline]
    pass


@admin.register(Photo)
class PhotoAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('number', 'album', 'preview')
    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{ obj.photo_url }" height="200">')


class PhotoInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Photo
    fields = []
    readonly_fields = ['preview']

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.photo_url}" height="200">')

    extra = 0


@admin.register(Photographer)
class PhotographerAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('number', 'name')
    pass


@admin.register(Album)
class AlbumAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ('number', 'name', 'photograph')
    form = AlbumAdminForm
    inlines = [PhotoInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)


@admin.register(About_U)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('id', 'isVisible')
    pass


@admin.register(Addres)
class AddresAdmin(admin.ModelAdmin):
    list_display = ('place', 'email')
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'phone', 'email')
    pass
