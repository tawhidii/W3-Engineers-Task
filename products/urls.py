from django.urls import path
from .views import(
    product_home,
    stripe_config,
    create_checkout_session,
    payment_success,
    payment_cancelled,
    stripe_webhook
)

app_name = 'products'

urlpatterns = [
    path('',product_home,name='product-home'),
    path('config/',stripe_config),
    path('create-chkout-session/',create_checkout_session,name='create-checkout-session'),
    path('success/',payment_success),
    path('cancelled/',payment_cancelled),
    path('webhook/',stripe_webhook)
]
