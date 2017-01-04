from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^prueba$/', views.index, name='index'),
    url(r'^home$/',views.mostrarPrincipal),
]
