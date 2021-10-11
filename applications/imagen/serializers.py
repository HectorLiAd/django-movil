from rest_framework import serializers
from drf_extra_fields.fields import HybridImageField
from . import models

class ImageSerializer(serializers.ModelSerializer):
    class Meta():
        model = models.Imagen
        fields = (
            'id',
            'created',
            'modified',
            'title',
            'detail',
            'image',
        )

class ImageCreateSerializer(serializers.ModelSerializer):
    image = HybridImageField(required=False)
    class Meta():
        model = models.Imagen
        fields = (
            'created',
            'modified',
            'title',
            'detail',
            'image',
        )