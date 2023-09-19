from django.shortcuts import render,get_object_or_404
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


def productDetail(request,slug):
    product = get_object_or_404(Product, slug=slug)
    template=loader.get_template("products/productDetail.html")

    return HttpResponse(template.render({'product':product},request))