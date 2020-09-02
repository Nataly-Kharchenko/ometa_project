from django.conf import settings
from django.contrib import admin

# Register your models here.


from .models import Photographer, Album, Photo, Director, Video, Work, About, Contact, Address


admin.site.register(Photographer)
admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(Director)
admin.site.register(Video)
admin.site.register(Work)
admin.site.register(About)
admin.site.register(Contact)
admin.site.register(Address)
