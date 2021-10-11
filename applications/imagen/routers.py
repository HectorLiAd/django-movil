from rest_framework.routers import DefaultRouter
# 
from . import viewsets
# code
routerImagenes = DefaultRouter()
routerImagenes.register(r'imagenes', viewsets.ImagenViewSet, basename='imagenes')

# url_Imagenes = routerImagenes.get_urls()

urlpatterns = routerImagenes.get_urls()