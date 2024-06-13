from django.test import TestCase
from django.urls import reverse
from .models import Hamburguesa

# V15
# Create your tests here. Los metodos deben empezar con la palabra test

class homePageTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)         #primer arg funcion que queremos testear, seg el result esperado


# Para cargar test usamos el comando python3 manage.py test

# Cliente es una funcion de python ese comando de self es visitar homepage en nuestro browser
# Si todo esta ok la respuesta es 200


class HamburguesaTestCase(TestCase):
    def test_newHamburguesa_added(self):
        numHamburguesa = Hamburguesa.objects.count() # Devuelve numero objetos hamb en BD
        
        # Aniadimos un nuevo obj
        Hamburguesa.objects.create(nombre='hamburguesa7', precio1=3500, precio2=4200, hImagen="url")
        
        # Si fue aniadida correctamente deberian coincidir
        self.assertEqual(Hamburguesa.objects.count(), numHamburguesa+1) 

        # Django crea una BD para testear que luego destruye
        # Osea usa una BD distinta para testear


# Se pueden testear muchas cosas mas que estan en la documentacion de Django