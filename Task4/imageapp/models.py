from django.db import models

class ImageModel(models.Model):
    original_image = models.ImageField(upload_to='originals/')
    bw_image = models.ImageField(upload_to='bw/', null=True, blank=True)

    def __str__(self):
        return f"Image {self.id}"
