from django.contrib import admin
from django.urls import path, include
from . import views
from herbatea.views import signin, signup, trackorder, orders


urlpatterns = [
   path('', views.home, name="home"),
   path('admin/', admin.site.urls, name = "admin"),
   path('', include('herbatea.urls')),
   path('signin/', signin, name = "sign_in"),
   path('signup/', signup, name = "sign_up"),
   path('trackorder/', trackorder, name = "track_order"),
   path('orders/', views.orders, name = "orders"),
]