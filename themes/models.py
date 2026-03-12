from django.db import models

# models forThemes.
class SiteSettings(models.Model):
    banner=models.ImageField(upload_to='media/site')
    caption=models.TextField()
    