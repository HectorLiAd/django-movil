from rest_framework import viewsets

from .models import Imagen
from . import serializers


class ImagenViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return Imagen.objects.all().order_by('-id')
        
        
    def get_serializer_class(self):
        if(self.action=='create' or self.action=='partial_update' or self.action=='update' ) :
            return serializers.ImageCreateSerializer
        else:
            return serializers.ImageSerializer