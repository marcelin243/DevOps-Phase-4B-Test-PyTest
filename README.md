# DevOps-Phase-4B-Test-PyTest
=================================
Voici les étapes pour créer une application Django, en commençant par l'installation de Python

Étape 1 : Installer Python
Avant de commencer avec Django, assurez-vous d'avoir Python installé sur votre machine. Vous pouvez télécharger Python à partir du site officiel :https://www.python.org/downloads/

Étape 2 : Installer Django
Une fois Python installé, vous pouvez installer Django avec pip. Ouvrez votre terminal ou votre invite de commande et exécutez : >> pip install django

Étape 3 : Créer un Nouveau Projet Django
Utilisez la commande suivante pour créer un nouveau projet Django. Remplacez myproject par le nom de votre projet. : >> django-admin startproject myproject

Étape 4 : Naviguer dans le Répertoire du Projet
Accédez au répertoire de votre projet : >> cd myproject

Étape 5 : Créer une Nouvelle Application
Django permet de créer des applications au sein d'un projet. Utilisez la commande suivante pour créer une nouvelle application. Remplacez myapp par le nom de votre application. >> python manage.py startapp myapp

Étape 6 : Configurer les Paramètres de l'Application
Ajoutez votre application à la liste des INSTALLED_APPS dans le fichier settings.py de votre projet : 
# myproject/settings.py

INSTALLED_APPS = [
    ...
    'myapp',
]

Étape 7 : Créer un Modèle
Dans le fichier models.py de votre application, définissez vos modèles. Par exemple, un modèle de produit :
# myapp/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

Étape 8 : Créer et Appliquer les Migrations
Générez les migrations pour le modèle que vous avez créé, puis appliquez-les à la base de données :
>>python manage.py makemigrations
>>python manage.py migrate

Étape 9 : Créer un Sérialiseur (pour les APIs)
Si vous créez une API, vous aurez besoin de sérialiseurs. Créez un fichier serializers.py dans votre application.

# myapp/serializers.py

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description']


Étape 10 : Créer des Vues
Dans le fichier views.py, définissez vos vues. Par exemple, une vue pour lister les produits :
# myapp/views.py

from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


Étape 11 : Configurer les URL
Dans le fichier urls.py de votre application, configurez les routes pour accéder à vos vues.
# myapp/urls.py


from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

Ensuite, incluez les URL de votre application dans le fichier urls.py principal :
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from myapp.urls import router as myapp_router

from rest_framework import routers

router=routers.DefaultRouter()

router.registry.extend(myapp_router.registry)

urlpatterns = [
    # re_path('admin/', admin.site.urls),
    re_path('', include(router.urls)),
    re_path('', include('myapp.urls'))
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


Étape 12 : Exécuter le Serveur de Développement
Exécutez le serveur de développement pour tester votre application : >> python manage.py runserver

Étape 13 : Accéder à l'API
Vous pouvez maintenant accéder à votre API à l'adresse suivante dans votre navigateur ou via un outil comme Postman :
http://127.0.0.1:8000/api/products/

Étape 14 : Créer des Tests
Créez des tests pour votre application dans le fichier tests.py de votre application : 
 
 cfr Document Word....

Avec ces étapes, vous avez créé une application Django simple avec un modèle, des vues, des sérialiseurs, des routes et des tests. Vous pouvez maintenant développer davantage votre application en ajoutant des fonctionnalités supplémentaires et en l'intégrant avec d'autres services.
