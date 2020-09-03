from django.conf import settings
from django.contrib import admin

# Register your models here.

from .models import Photographer, Album, Photo, Director, Video, Work, About_U, Contact, Addres, Preview_Video


admin.site.register(Photographer)

admin.site.register(Director)
admin.site.register(Video)
admin.site.register(Work)
admin.site.register(About_U)
admin.site.register(Contact)
admin.site.register(Addres)
admin.site.register(Preview_Video)


class PhotoAdmin(admin.ModelAdmin):
    pass


class PhotoInline(admin.StackedInline):
    model = Photo
    max_num = 50
    extra = 0


class AlbumAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
