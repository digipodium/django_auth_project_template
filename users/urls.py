from django.conf.urls import include
from django.urls import path

from .views import dashboard, register

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('oauth/', include('social_django.urls')),
]