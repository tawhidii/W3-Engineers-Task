from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import Product
import stripe
from django.template import loader
# Product home fuction based view 
def product_home(request):
    products = Product.objects.only('title','image','price')
    context = {
        'products': products
    }
    template_name = 'products/product_home.html'
    return render(request,template_name,context)


# Stripe config view 
@csrf_exempt
def stripe_config(request):
    if request.method == 'GET':
        stripe_config = {'public_key':settings.STRIPE_PUBLISHABLE_KEY }
        return JsonResponse(stripe_config,safe=False)



# Create checkout session view 
@csrf_exempt
def create_checkout_session(request):
   
    if request.method == 'GET':
        
        domain_url = 'http://localhost:8000/'
        stripe.api_key = settings.STRIPE_SECRET_KEY
        try:
            title = request.GET.get('title')
            price = request.GET.get('price')
            print(price)
            checkout_session = stripe.checkout.Session.create(
                success_url=domain_url + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {   
                        'name': f'{title}',
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': f'{price}',
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})
