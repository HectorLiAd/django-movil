from django.urls import path, include

urlpatterns = [
    path(
        '',
        include('applications.imagen.routers'),
    ),
]