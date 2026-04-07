
SECRET_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
DEBUG=False
ALLOWED_HOSTS = ['mondomaine.fr', 'www.mondomaine.fr']
CSRF_TRUSTED_ORIGINS = ["https://mondomaine.fr", "https://www.mondomaine.fr"]
STATIC_ROOT = "/app/demo/staticfiles"
MEDIA_ROOT = "/app/demo/media"

# token Huggingface
HF_TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"