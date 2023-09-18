from django.contrib import admin
from .models import User, Category, Colour,ProductImage,Product,Accessories,ComputerAndPhone,Clothe,HomeLiving,BeautyPersonalCare,SportsOutdoors,ElectronicsBrand,ClotheBrand,HomeLivingBrand,BeautyPersonalCareBrand,SportsOutdoorsBrand

# Register your models here.

# User Model 
class UserAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name")

admin.site.register(User,UserAdmin)

# Product Model 
class ProductAdmin(admin.ModelAdmin):
  list_display = ("name", "category", "slug","main_image","created_at",)
  prepopulated_fields = {"slug": ["name"]}

admin.site.register(Product,ProductAdmin)

# Category Model 

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
 
admin.site.register(Category,CategoryAdmin)


# Brand Model 

class ElectronicsBrandAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
 
admin.site.register(ElectronicsBrand,ElectronicsBrandAdmin)


class ClotheBrandAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
 
admin.site.register(ClotheBrand,ClotheBrandAdmin)


class HomeLivingBrandAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
 
admin.site.register(HomeLivingBrand,HomeLivingBrandAdmin)

class BeautyPersonalCareBrandAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
 
admin.site.register(BeautyPersonalCareBrand,BeautyPersonalCareBrandAdmin)


class SportsOutdoorsBrandAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
 
admin.site.register(SportsOutdoorsBrand,SportsOutdoorsBrandAdmin)
# Colour Model 

class ColourAdmin(admin.ModelAdmin):
    list_display = ("name",)
 
admin.site.register(Colour,ColourAdmin)

#  ProductImage Model 

admin.site.register(ProductImage)

# Electronics
class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
 
admin.site.register(Accessories,AccessoriesAdmin)


# ComputerAndPhone Model 
class ComputerAndPhoneAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
 
admin.site.register(ComputerAndPhone,ComputerAndPhoneAdmin)

# Clothe Model 
class ClotheAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
 
admin.site.register(Clothe,ClotheAdmin)

# HomeLiving Model 
class HomeLivingAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
 
admin.site.register(HomeLiving,HomeLivingAdmin)

# BeautyPersonalCare Model 
class BeautyPersonalCareAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
 
admin.site.register(BeautyPersonalCare,BeautyPersonalCareAdmin)

# SportsOutdoors Model 
class SportsOutdoorsAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
 
admin.site.register(SportsOutdoors,SportsOutdoorsAdmin)


