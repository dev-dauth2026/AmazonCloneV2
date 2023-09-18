from django.contrib import admin
from .models import User, Category, Product,ProductImage

# Register your models here.
class UserAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name")

admin.site.register(User,UserAdmin)

class ProductAdmin(admin.ModelAdmin):
  list_display = ("name", "category", "slug","main_image","created_at",)
  prepopulated_fields = {"slug": ["name"]}

admin.site.register(Product,ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
 
admin.site.register(Category,CategoryAdmin)

admin.site.register(ProductImage)

