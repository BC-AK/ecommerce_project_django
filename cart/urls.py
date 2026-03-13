from django.urls import path
from .views import cart_view, add_to_cart, increase_quantity, decrease_quantity, remove_item

urlpatterns = [

path('', cart_view, name='cart'),

path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),

path('increase/<int:cart_id>/', increase_quantity, name='increase_quantity'),

path('decrease/<int:cart_id>/', decrease_quantity, name='decrease_quantity'),

path('remove/<int:cart_id>/', remove_item, name='remove_item'),

]