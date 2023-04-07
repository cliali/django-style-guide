from config.env import env

DEFAULT_FROM_EMAIL = 'default@cliali.com'

ADMINS = [
    ('cliali', 'admin@cliali.com')
]

EMAIL_HOST = env('EMAIL_HOST', default='smtp4dev')
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')
EMAIL_PORT = env('EMAIL_PORT', default=2525)