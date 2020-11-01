from rest_framework.response import Response
from rest_framework.views import APIView

from .views import *
from .serializers import *


class PreviewVideosView(APIView):
    def get(self, request):
        preview_video_list = get_object_or_404(Preview_Video.objects.all(), isVisible=True)
        serializer = PreviewVideosSerializer(preview_video_list, many=True)
        return Response({"preview_videos": serializer.data})


class WorksView(APIView):
    def get(self, request):
        work_list = Work.objects.all()
        serializer = WorksSerializer(work_list, many=True)
        return Response({"works": serializer.data})


class DirectorsView(APIView):
    def get(self, request):
        director_list = Director.objects.all()
        serializer = DirectorsSerializer(director_list, many=True)
        return Response({"directors": serializer.data})


class DirectorArtistView(APIView):
    def get(self, request, id):
        director = get_object_or_404(Director.objects.all(), id=id)
        video_list = Video.objects.filter(director=id)
        dir_serializer = DirectorsSerializer(director, many=False)
        video_serializer = VideosSerializer(video_list, many=True)
        return Response({"director": dir_serializer.data, "videos": video_serializer.data})


class PhotographersView(APIView):
    def get(self, request):
        photographer_list = Photographer.objects.all()
        serializer = PhotographersSerializer(photographer_list, many=True)
        return Response({"photographers": serializer.data})


class PhotoArtistView(APIView):
    def get(self, request, id):
        photographer = get_object_or_404(Photographer.objects.all(), id=id)
        album_list = Album.objects.filter(photograph=id)
        photo_list = []
        for obj in album_list:
            photos = Photo.objects.filter(album=obj.id)
            for ph_obj in photos:
                photo_list.append(ph_obj)
        photographer_serializer = PhotographersSerializer(photographer, many=False)
        album_serializer = AlbumsSerializer(album_list, many=True)
        photo_serializer = PhotosSerializer(photo_list, many=True)
        return Response({"photographer": photographer_serializer.data, "albums": album_serializer.data, "photos": photo_serializer.data})


class AboutUsView(APIView):
    def get(self, request):
        about_us_list = get_object_or_404(About_U.objects.all(), isVisible=True)
        serializer = AboutUsSerializer(about_us_list, many=False)
        return Response({"about_us": serializer.data})


class ContactsView(APIView):
    def get(self, request):
        address_list = Addres.objects.all()
        address_serializer = AddressSerializer(address_list, many=True)
        contact_list = Contact.objects.all()
        contacts_serializer = ContactsSerializer(contact_list, many=True)
        return Response({"address": address_serializer, "contacts": contacts_serializer.data})
