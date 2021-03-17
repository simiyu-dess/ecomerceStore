from django.shortcuts import render, get_object_or_404, redirect
from Categories.models import Category
from .models import Product, Brand
from cart.forms import cartAddProductForm


# Create your views here.
def home_pageview(request):
    
    brands=Brand.objects.all()
    categories=Category.objects.all()
    products= Product.objects.all()
    
    
    
    context = {
        'brands':brands,
        'categories':categories,
        'products':products
    }
    
    return render(request,'index.html',context)

    


def products_list(request, category_slug=None, brand_slug=None):
    category=None
    brand=None
    
    
    categories=Category.objects.all()
    brands=Brand.objects.all()
    products=Product.objects.filter(is_active=True)

        
    if category_slug:
        category=get_object_or_404(Category, category_slug=category_slug)
        products=Product.objects.filter(category=category)
        
   
        
    context={
        'brands':brands,
        'category':category,
        'categories':categories,
        'products':products
        
    }
    
    return render(request,"product-list.html", context)
    
        

def product_detail(request,id,product_slug):
    categories=Category.objects.all()
    products=Product.objects.all()
    brands=Brand.objects.all()
    product=get_object_or_404(Product,id=id, product_slug=product_slug, is_active=True)
    cart_add_product_form = cartAddProductForm()
    context={
        'product':product,
        'brands':brands,
        'categories':categories,
        'products':products,
        'cart_add_product_form':cart_add_product_form
    }
    
    return render(request, "product-detail.html",context)

def products_list_by_brand_view(request, brand_slug=None):
    brand=None
    category=None
    
    brands=Brand.objects.all()
    products=Product.objects.filter(is_active=True)
    
    if brand_slug:
        brand=get_object_or_404(Brand,brand_slug=brand_slug)
        products=Product.objects.filter(brand=brand)
        
        
    context={
        'brand':brand,
        'brands':brands,
        'products':products
        
    }
    
    
    return render(request, "product-list-category.html", context)

    

    
    
    
    
    