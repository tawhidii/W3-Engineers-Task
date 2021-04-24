from django.urls import path
from .views import product_home

app_name = 'products'

urlpatterns = [
    path('',product_home,name='product-home')
]
