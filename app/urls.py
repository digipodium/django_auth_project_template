from django.urls import path
from .views import index,purchase_item
from app import views

urlpatterns = [
    path('',index,name='home'),
    path('purchase/',purchase_item,name="purchase"),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path('product/detail/<int:pk>',views.show_single_product,name='product_detail'),
    path('product/all',views.show_products,name='product_all'),
]