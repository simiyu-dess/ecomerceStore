from django.contrib import admin
from Products.models import Product , Brand
from Categories.models import Category
from Products.forms import ProductAdminForm

class AdminProduct(admin.ModelAdmin):
    form = ProductAdminForm
    
    list_display = ('product_name', 'price', 'old_price', 'created_at', 'updated_at',)
    list_display_links=('product_name',)
    list_per_page=50
    ordering=['-created_at']
    search_fields=['product_name','product_price','meta_keywords','meta_description']
    exclude=('created_at','updated_at',)
    prepopulated_fields={'product_slug':('product_name',)}
    
admin.site.register(Product,AdminProduct)


class CategoryAdmin(admin.ModelAdmin):
    list_display=('category_name','created_at','updated_at',)
    list_display_links=('category_name',)
    list_per_page=20
    ordering=['category_name']
    search_fields=['category_name','description','meta_keywords','meta_description']
    exclude=('created_at','updated_at')
    prepopulated_fields={'category_slug':('category_name',)}
admin.site.register(Category,CategoryAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display=('brand_name',)
    list_display_links=('brand_name',)
    list_per_page=10
    ordering=['brand_name']
    search_fields=['brand_name']
    prepopulated_fields={'brand_slug':('brand_name',)}
    
admin.site.register(Brand,BrandAdmin)
    
    
    
    

# Register your models here.
