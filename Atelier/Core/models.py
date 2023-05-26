from django.db import models

def uploader_path(instance, filename):
    return "/".join(["imagens", str(instance.desc_imagem), filename])

# Create your models here.
class ImagensAtelier(models.Model):
    desc_imagem = models.CharField(max_length=50)
    imagem =models.ImageField(blank=True, null=True, upload_to=uploader_path)