from django.urls import path
from .views import checkout, place_order, order_success

urlpatterns = [

path('checkout/', checkout, name='checkout'),

path('place-order/', place_order, name='place_order'),

path('success/', order_success, name='order_success'),

]