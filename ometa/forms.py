from django import forms
from django.core.validators import validate_image_file_extension
from django.utils.translation import gettext as _


from .models import Album, Photo


class AlbumAdminForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = (
            "number",
            "name",
            "photograph"
        )

    photos = forms.FileField(
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
        label=_("Add photos"),
        required=False,
    )

    def clean_photos(self):
        """Make sure only images can be uploaded."""
        for upload in self.files.getlist("photos"):
            validate_image_file_extension(upload)

    def save_photos(self, album):
        """Process each uploaded image."""
        for upload in self.files.getlist("photos"):
            photo = Photo(album=album, photo=upload)
            photo.save()
