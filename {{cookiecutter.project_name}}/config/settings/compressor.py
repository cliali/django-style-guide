import os

from config.env import BASE_DIR

COMPRESS_ROOT = os.path.join(BASE_DIR, "static")

COMPRESS_ENABLED = True

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)
