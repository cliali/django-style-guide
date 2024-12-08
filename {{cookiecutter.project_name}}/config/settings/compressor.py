import os

from config.env import BASE_DIR

COMPRESS_ROOT = os.path.join(BASE_DIR, "static")

COMPRESS_ENABLED = True

STATICFILES_FINDERS = ("compressor.finders.CompressorFinder",)
