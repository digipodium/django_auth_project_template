from django.urls import path
from .views import index,purchase_item

urlpatterns = [
    path('',index,name='home'),
    path('purchase/',purchase_item,name="purchase")
]