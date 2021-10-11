from django.db import models
from django.db.models.fields.files import ImageField

from model_utils.models import TimeStampedModel

# Create your models here.
class Imagen(TimeStampedModel):
    title = models.CharField(max_length=60)
    detail = models.TextField(blank=True, null=True)

    image = models.ImageField('Imagen de prueba',upload_to='imagen', blank=True, null=True)
    
    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'

    def __str__(self):
        return str(self.id) + ' ' + str(self.title)