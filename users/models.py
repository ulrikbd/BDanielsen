from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image)

        # for orientation in ExifTags.TAGS.keys():
        #     if ExifTags.TAGS[orientation] == 'Orientation':
        #         break
        # exif = dict(img._getexif().items())
        #
        # if exif[orientation] == 3:
        #     img = img.rotate(180, expand=True)
        # elif exif[orientation] == 6:
        #     img = img.rotate(270, expand=True)
        # elif exif[orientation] == 8:
        #     img = img.rotate(90, expand=True)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)

            thumb_io = BytesIO()
            img.save(thumb_io, img.format)
            file_name = self.image.name
            self.image.save(
                file_name,
                ContentFile(
                    thumb_io.getvalue()),
                save=False)
            super().save(*args, **kwargs)

    #
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
