from django.urls import path
from .views import(
    product_home,
    stripe_config,
    create_checkout_session
)

app_name = 'products'

urlpatterns = [
    path('',product_home,name='product-home'),
    path('config/',stripe_config),
    path('create-chkout-session/',create_checkout_session,name='create-checkout-session')
]
