from django.urls import path
from . import views

urlpatterns = [
	##path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('', views.products, name='products'),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('contact/', views.contact, name="contact"),
	path('thankyou/', views.thankyou, name="thankyou"),
	path('login/', views.loginPage, name="login"),
	path('signup/', views.signup, name="signup"),
	path('register/', views.registerPage, name="register"),
	path('placedorder/', views.placedorder, name="placedorder"),
	path('logout/', views.logoutUser, name="logout"),
	path('update_item/', views.updateItem, name="update_item"),



]