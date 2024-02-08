from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [

  path('cart',views.show_cart,name='cart'),
  path('add_to_cart',views.add_to_cart,name='add_to_cart'),
  path('remove_item/<pk>',views.remove_item,name='remove_item'),
  path('check_out',views.checkout_cart,name='check_out'),
  path('orders',views.show_orders,name='orders')
]
