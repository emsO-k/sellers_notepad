# sellers_notepad
A small notes web app with two basic fields: a client name and notes. This app is primarily thought to be used by individuals with small/medium size businesses in which they have requests/orders from clients to be fulfilled.

# Deploy in pythonanywhere instructions
### Activate your virtual environment and do a `pip install whitenoise`
Modify the `settings.py` with

`DEBUG = False`

`ALLOWED_HOSTS = ['yoururl.pythonanywhere.com']`

`MIDDLEWARE = [
    ...
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]`

`STATIC_ROOT = BASE_DIR / "staticfiles"`

Run `python manage.py collectstatic`

Reload the application