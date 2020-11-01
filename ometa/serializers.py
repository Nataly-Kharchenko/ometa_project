from rest_framework import serializers


class PreviewVideosSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    video = serializers.FileField()
    isTitle = serializers.BooleanField()


class WorksSerializer(serializers.Serializer):
    number = serializers.IntegerField(default=1)
    name = serializers.CharField(max_length=120)
    choice_player = serializers.CharField(max_length=7)
    link_for_video = serializers.CharField(max_length=120)
    description = serializers.CharField()


class DirectorsSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    preview = serializers.ImageField()


class VideosSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    choice_player = serializers.CharField(max_length=7)
    link_for_video = serializers.CharField(max_length=120)
    director = serializers.CharField()
    director_id = serializers.IntegerField()
    description = serializers.CharField()


class PhotographersSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    name = serializers.CharField(max_length=30)


class AlbumsSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    photograph = serializers.CharField()
    photograph_id = serializers.IntegerField()


class PhotosSerializer(serializers.Serializer):
    number = serializers.IntegerField()
    album = serializers.CharField()
    album_id = serializers.IntegerField()
    photo = serializers.ImageField()
    isTitle = serializers.BooleanField()


class AboutUsSerializer(serializers.Serializer):
    information = serializers.CharField()
    isVisible = serializers.BooleanField()


class AddressSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=30)
    place = serializers.CharField(max_length=120)
    link_for_google_maps = serializers.CharField(max_length=120)


class ContactsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    position = serializers.CharField(max_length=30)
    phone = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30)
