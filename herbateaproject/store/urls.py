from . import views
from django.urls import path


urlpatterns = [
   path('', views.home, name="home"),
   path('about/', views.about, name='about'),
   path('signin/', views.signin, name = "sign_in"),
   path('signup/', views.signup, name = "sign_up"),
   path('trackorder/', views.trackorder, name = "track_order"),
   path('orders/', views.orders, name = "orders"),
   path('contact/', views.contact, name="contact"),
	path('thankyou/', views.thankyou, name="thankyou"),
]