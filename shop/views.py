from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse    
from django.template import loader
from .models import Product,Category,Clothe


# Create your views here.
def home(request):
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


# def addToCart(request,productId):
#     product = get_object_or_404(Product, id=productId)
#     # cart, created = Cart.objects.get_or_create(user=user)

#     if request.method=="POST":
#         selectedSize = None

#         if isinstance(product,Clothe):
#             selectedSize = request.POST.get('selectedSize')
        
#         cart =request.session.get('cart',{})
#         if productId in cart:
#             cart[productId]['quantity']+=1
        
#         else:
#             cart[productId]={'selectedSize':selectedSize,'quantity':1}

#         request.session['cart']= cart
    

#     return redirect('/')
    

