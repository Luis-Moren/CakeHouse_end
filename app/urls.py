from django.urls import path
from .views import home, contacto, galeria, agregar_producto, modificar_producto

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
]