from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name='main'),
    path('shop/', shop, name='shop'),
    path('cart/', cart, name='cart'),
    path('delete_cart_item/<int:pk>', delete_cart_item, name='delete_cart_item'),
    path('edit_cart_item/<int:pk>', edit_cart_item, name='edit_cart_item'),
    path('search_page', search_page, name='search_page'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),
    path('cart/make_order', make_order, name='make_order'),
    path('orders/', orders, name='orders'),
    path('delete_review/<int:pk>/', delete_review, name='delete_review'),
    path('edit_review/<int:pk>/', edit_review, name='edit_review'),

]
