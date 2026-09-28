from django.db import models


class Planet(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    order = models.IntegerField()
    base_color = models.CharField(max_length=20, default="#4fd8ff")
    icon = models.CharField(max_length=50, default="fa-solid fa-globe")
    tagline = models.CharField(max_length=255)

    # Rasmlar (Teksturalar)
    texture = models.ImageField(upload_to='planets/textures/')
    ring_texture = models.ImageField(upload_to='planets/rings/', blank=True, null=True)

    def __string__(self):
        return self.name