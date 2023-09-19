from django.urls import path
from . import views

urlpatterns = [
    path('',views.shop, name='shop'),
    path('productDetail/<slug:slug>', views.productDetail, name='productDetail')
]
