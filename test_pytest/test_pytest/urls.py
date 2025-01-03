"""
URL configuration for test_pytest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

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