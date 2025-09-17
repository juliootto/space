from cloudinary_storage.storage import StaticHashedCloudinaryStorage

class MyStaticHashedCloudinaryStorage(StaticHashedCloudinaryStorage):
    def _get_url(self, name):
        """
        Overrides the method to ensure paths use forward slashes for Cloudinary.
        """
        print(f"Caminho do arquivo sendo processado: {name}")
        print(f"Caminho do arquivo sendo processado: {super()._get_url(name).replace('%5C', '/')}")
        return super()._get_url(name).replace('%5C', '/')