from django.shortcuts import render, get_object_or_404

from ometa.models import Photographer, Album, Photo, Director, Video, Work, About, Contact, Address


def home(request):
    return render(request, "partials/index.html")


def works(request):
    works_list = Work.objects.all()

    context = {
        "works": works_list
    }
    return render(request, "partials/works.html", context)


def directors(request):
    director_artists = Director.objects.all()

    if director_artists:
        context = {
            "directors": director_artists,
            "active_director": director_artists[0]
        }
        return render(request, "partials/directors.html", context)
    else:
        return render(request, "partials/directors.html")


def director_artist(request, id=None):
    director = get_object_or_404(Director, id=id)
    videos = Video.objects.filter(director=id)

    context = {
        "director": director,
        "videos": videos
    }
    return render(request, "partials/director-artist.html", context)


def photographers(request):
    photo_artists = Photographer.objects.all()
    preview_photo = Photo.objects.filter(isTitleImg='1')
    preview_photo_list = []
    for ar_obj in photo_artists:
        for ph_obj in preview_photo:
            if ar_obj.id == ph_obj.album.photograph.id:
                preview_photo_list.append(ph_obj)

    if preview_photo_list and photo_artists:
        context = {
            "photo_artists": photo_artists,
            "photos": preview_photo_list,
            "active_photo": preview_photo_list[0],
            "active_artist": photo_artists[0]
        }
        return render(request, "partials/photographers.html", context)
    else:
        return render(request, "partials/photographers.html")


def photo_artist(request, id=None):
    artist = get_object_or_404(Photographer, id=id)
    albums_list = Album.objects.filter(photograph=id)
    photo = Photo.objects.all()

    first_photo_list = []
    photo_list = []
    photos = []
    i = 0

    for al_obj in albums_list:
        for ph_obj in photo:
            if ph_obj.album.id == al_obj.id:
                if ph_obj.number == '1':
                    first_photo_list.append(ph_obj)
                photos.append(ph_obj)
        photos.sort(key=lambda x: x.number)
        photo_list.append([])
        for obj in photos:
            photo_list[i].append(obj)
        photos.clear()
        i += 1

    context = {
        "artist": artist,
        "active_photos": first_photo_list,
        "photos": photo_list
    }
    return render(request, "partials/photo-artist.html", context)


def about_us(request):
    information = About.objects.get(isVisible=True)

    context = {
        "about_us": information
    }
    return render(request, "partials/about.html", context)


def contacts(request):
    contact_list = Contact.objects.all()
    address_list = Address.objects.all()

    context = {
        "contacts": contact_list,
        "addresses": address_list,
    }
    return render(request, "partials/contacts.html", context)
