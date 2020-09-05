import os

from django.db import models, transaction
from phonenumber_field.modelfields import PhoneNumberField
from sorl.thumbnail.templatetags.thumbnail import thumbnail


class Preview_Video(models.Model):
    name = models.CharField(max_length=30, default='No name')
    video = models.FileField(upload_to='preview_video', null=True, blank=True)
    isTitle = models.BooleanField(default=True)

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.isTitle:
            Preview_Video.objects.filter(isTitle=True).update(isTitle=False)
        super(Preview_Video, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    @property
    def video_url(self):
        if self.video and hasattr(self.video, 'url'):
            return self.video.url


class Work(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=120)
    YOUTUBE = 'YouTube'
    VIMEO = 'vimeo'
    PLAYER_CHOICES = [
        (YOUTUBE, 'YouTube'),
        (VIMEO, 'vimeo')
    ]
    choice_player = models.CharField(max_length=7, choices=PLAYER_CHOICES, default=VIMEO)
    link_for_video = models.CharField(max_length=120, default='Video is not loaded')
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta(object):
        ordering = ['number']


class Director(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=30, default='No name')
    preview = models.ImageField(upload_to='directors_preview', null=True, blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "directors/%i/" %(self.id)

    @property
    def preview_url(self):
        if self.preview and hasattr(self.preview, 'url'):
            return self.preview.url

    class Meta(object):
        ordering = ['number']

    def preview_image_url(self):
        image_path = thumbnail(self.image, '60x60')
        image_path = image_path.replace('\\', '/')  # Windows-Fix
        return '<a href="' + str(self.id) + '/"><img src="' + str(self.preview_url) + '"/></a>'

    preview_image_url.short_description = 'Thumbnail'
    preview_image_url.allow_tags = True


class Video(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=50, default='No name')
    YOUTUBE = 'YouTube'
    VIMEO = 'vimeo'
    PLAYER_CHOICES = [
        (YOUTUBE, 'YouTube'),
        (VIMEO, 'vimeo')
    ]
    choice_player = models.CharField(max_length=7, choices=PLAYER_CHOICES, default=VIMEO)
    link_for_video = models.CharField(max_length=120, default='Video is not loaded')
    director = models.ForeignKey(Director, on_delete=models.CASCADE, default=1, related_name='director')
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "Director:" + str(self.director.name) + ", video:" + str(self.name)

    def __str__(self):
        return "Director:" + str(self.director.name) + ", video:" + str(self.name)

    class Meta(object):
        ordering = ['number']


class Photographer(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=30, default='No name')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "photographers/%i/" %(self.id)

    class Meta(object):
        ordering = ['number']


class Album(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=30)
    photograph = models.ForeignKey(Photographer, on_delete=models.CASCADE, default=1, related_name="photograph")

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta(object):
        ordering = ['number']


class Photo(models.Model):
    number = models.IntegerField(default=0)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="photos")
    photo = models.ImageField(upload_to="photo/", default='', null=True, blank=True)
    isTitle = models.BooleanField(default=0)

    def __unicode__(self):
        return str(self.photo)

    def __str__(self):
        return str(self.photo)

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    class Meta(object):
        ordering = ['number']


class About_U(models.Model):
    information = models.TextField(null=True, blank=True)
    isVisible = models.BooleanField(default=True)

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.isVisible:
            About_U.objects.filter(isVisible=True).update(isVisible=False)
        super(About_U, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)


class Addres(models.Model):
    email = models.EmailField(max_length=30, default='No email')
    place = models.CharField(max_length=120, default='No address')
    link_for_google_maps = models.CharField(max_length=120, default='No link')

    def __unicode__(self):
        return self.place

    def __str__(self):
        return self.place


class Contact(models.Model):
    name = models.CharField(max_length=30, default='No name')
    position = models.CharField(max_length=30, default='No position')
    phone = PhoneNumberField(default='No phone number')
    email = models.EmailField(max_length=30, default='No email')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name
