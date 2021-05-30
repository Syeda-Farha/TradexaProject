from django.shortcuts import render
from . models import Product

# Create your views here.
def products(request):
    products= None
    products = Product.objects.all()
    data = {}
    data['products'] = products

    return render(request,'products.html',data)