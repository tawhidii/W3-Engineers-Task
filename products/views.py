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
            title = request.GET.get('title',None)
            price = request.GET.get('price',None)
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



# Payment sucess view 
def payment_success(request):
    context = {}
    template_name = 'products/payment_success.html'
    return render(request,template_name,context)


# Payment cancelled view 
def payment_cancelled(request):
    context = {}
    template_name = 'products/payment_cancelled.html'
    return render(request,template_name,context)



    
@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_SECRET
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        print("Payment was successful.")

    return HttpResponse(status=200)