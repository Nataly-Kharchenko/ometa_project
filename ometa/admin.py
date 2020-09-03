from django.conf import settings
from django.contrib import admin

# Register your models here.


from .models import Photographer, Album, Photo, Director, Video, Work, About_U, Contact, Addres, Preview_Video


admin.site.register(Photographer)
admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Director)
admin.site.register(Video)
admin.site.register(Work)
admin.site.register(About_U)
admin.site.register(Contact)
admin.site.register(Addres)
admin.site.register(Preview_Video)
