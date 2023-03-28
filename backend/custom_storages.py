from storages.backends.s3boto3 import S3Boto3Storage
import io
from PIL import Image, ImageOps
import os
from backend.apps.core.images import *


class StaticStorage(S3Boto3Storage):
    
    bucket_name = 'novagenesisnz'
    location = 'static'

class MediaStorage(S3Boto3Storage):
    bucket_name = 'novagenesisnz'
    location = 'media'
    file_overwrite = False
    
    def _save(self, name, content):
        if hasattr(content, 'content_type') and content.content_type.startswith('image/'):  # noqa
            return self.generate_thumbnails(name, content)
        else:
            return super()._save(name, content)

    def _save_image(self, picture, filename, quality=100):
        fh = self.open(filename, 'wb')
        sfile = io.BytesIO()

        picture.save(sfile, format='jpeg', quality=quality)

        fh.write(sfile.getvalue())
        fh.close()

    def generate_thumbnails(self, filename, content):
        # _, ext = os.path.splitext(filename).lower()
        pic = Image.open(content)
        
        main_image = homothetical_transformation(pic)
        self._save_image(main_image, filename, 85)

        return filename