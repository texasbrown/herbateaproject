from django.contrib import admin
from django.urls import path, include


path('admin/', admin.site.urls),
path('', include('herbatea.urls')),
