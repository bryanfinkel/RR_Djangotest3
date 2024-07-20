"""
URL configuration for core project.

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
from django.urls import path
from mymap.views import index, school_map, get_nearby_schools, upload_csv

urlpatterns = [
    path('', index, name='mymap-index'),
    path('admin/', admin.site.urls),
    path('map/', school_map, name='school_map'),
    path('get_nearby_schools/<lat>/<lon>/', get_nearby_schools, name='get_nearby_schools'),
    path('upload_csv/', upload_csv, name='upload_csv'),
]
