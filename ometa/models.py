import os

from django.db import models, transaction
from phonenumber_field.modelfields import PhoneNumberField


class Photographer(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=30, default='No name')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "photographers/%i/" %(self.id)


class Album(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=30, default="No name")
    photograph = models.ForeignKey(Photographer, on_delete=models.CASCADE, default=0, related_name="photograph")

    def __unicode__(self):
        return "Photographer: " + str(self.photograph.name) + ", album: " + str(self.name)

    def __str__(self):
        return "Photographer: " + str(self.photograph.name) + ", album: " + str(self.name)

    def get_absolute_url(self):
        return "/%s/" %(self.id)


class Photo(models.Model):
    number = models.IntegerField(default=0)
    photo = models.ImageField(null=True, blank=True, upload_to="photo/")
    album = models.ForeignKey(Album, on_delete=models.CASCADE, default=1, related_name="album")
    isTitleImg = models.BooleanField(default=0)

    def __unicode__(self):
        return "Photographer: " + str(self.album.photograph.name) + ", album: " + str(self.album.name) + ", photo: " + str(self.number)

    def __str__(self):
        return "Photographer: " + str(self.album.photograph.name) + ", album: " + str(self.album.name) + ", photo: " + str(self.number)

    def get_absolute_url(self):
        return "directors/%i/" %(self.id)

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url


class Director(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=30, default='No name')
    preview = models.ImageField(upload_to='directors preview', null=True, blank=True)

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

    def get_absolute_url(self):
        return "/%s/" %(self.id)


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

    def get_absolute_url(self):
        return "/%s/" %(self.id)


class About(models.Model):
    information = models.TextField(null=True, blank=True)
    isVisible = models.BooleanField(default=True)

    @transaction.atomic
    def save(self, *args, **kwargs):
        if self.isVisible:
            About.objects.filter(isVisible=True).update(isVisible=False)
        super(About, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return "/%s/" %(self.id)


class Contact(models.Model):
    name = models.CharField(max_length=30, default='No name')
    position = models.CharField(max_length=30, default='No position')
    phone = PhoneNumberField(default='No phone number')
    email = models.EmailField(max_length=30, default='No email')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/%s/" %(self.id)


class Address(models.Model):
    email = models.EmailField(max_length=30, default='No email')
    place = models.CharField(max_length=120, default='No address')
    link_for_google_maps = models.CharField(max_length=120, default='No link')

    def __unicode__(self):
        return self.place

    def __str__(self):
        return self.place

    def get_absolute_url(self):
        return "/%s/" %(self.id)
