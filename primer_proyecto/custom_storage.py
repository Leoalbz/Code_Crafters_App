from storages.backends.gcloud import GoogleCloudStorage
from django.conf import settings

GS_BUCKET_NAME = "bucket-28-02-2025"

class GoogleCloudStaticStorage(GoogleCloudStorage):
    location = "static"  # Carpeta en el bucket
    bucket_name = GS_BUCKET_NAME
    file_overwrite = True  # Permite sobrescribir archivos estáticos

class GoogleCloudMediaStorage(GoogleCloudStorage):
    location = "media"  # Carpeta en el bucket
    bucket_name = GS_BUCKET_NAME
    file_overwrite = False