from django.urls import path
from . import views
app_name = 'shop' 
urlpatterns = [
    path('',views.home, name='home'),
    path('productDetail/<slug:slug>', views.productDetail, name='productDetail'),
    # path('addToCart/<int:pk',views.addToCart, name='addToCart')

]
