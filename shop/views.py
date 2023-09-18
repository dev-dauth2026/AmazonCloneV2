from django.shortcuts import render
from django.http import HttpResponse    
from django.template import loader
from .models import Product,Category


# Create your views here.
def shop(request):
    categories =Category.objects.all()
    category_products=[]
    for category in categories:
        products =Product.objects.filter(category=category)
        category_products.append({'category':category,'products':products})
    template= loader.get_template("main.html")

    return HttpResponse (template.render({'category_products':category_products},request))