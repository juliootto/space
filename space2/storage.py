from cloudinary_storage.storage import StaticCloudinaryStorage
import platform

class MyStaticCloudinaryStorage(StaticCloudinaryStorage):
    def _get_url(self, name):
        """
        Overrides the method to ensure paths use forward slashes for Cloudinary.
        """
        if platform.system() == 'Windows':
            name = name.replace('\\', '/')  
        return super()._get_url(name)