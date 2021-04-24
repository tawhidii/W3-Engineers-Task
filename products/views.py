from django.shortcuts import render

# Product home fuction based view 
def product_home(request):
    context = {

    }
    template_name = 'products/product_home.html'
    return render(request,template_name,context)
    