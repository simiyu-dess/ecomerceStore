from django.db import models
from Categories.models import Category
from django.urls import reverse

# Create your models here.
class Brand(models.Model):
    brand_name=models.TextField()
    brand_slug=models.SlugField(max_length=255, 
                         unique=True, 
                         help_text="Unique value for the product created from brand_name")
    
    class Meta:
        db_table="Brands"
        
        
    def __unicode__(self):
        return self.brand_name
    
    def get_abosolute_url(self):
        return reverse('brand_slug', args=[self.brand_slug])
    
    
class Product(models.Model):
    product_name=models.TextField(blank=False)
    product_slug=models.SlugField(max_length=255, unique=True,
                          help_text="Unique value for products, created from the products name")
    brand_name=models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_description=models.CharField(max_length=100, blank=False)
    meta_keywords=models.CharField("Meta Keywords",
                                   max_length=255,
                                   help_text="Content for the meta keywords")
    meta_description=models.CharField("Meta description",
                                      max_length=255,
                                      help_text="Content for the Meta description")
    sku=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=9,decimal_places=2,default=0.00)
    old_price=models.DecimalField(max_digits=9,decimal_places=2, null=True,blank=True)
    is_active=models.BooleanField(default=True)
    is_featured=models.BooleanField(default=False)
    product_image_one=models.FileField(upload_to='imagefiles',
                                       blank=True,
                                       help_text="The first image for the prouct")
    product_image_two=models.FileField(upload_to='imagefiles', 
                                       blank=True,
                                       help_text="Another image for the product")
    product_image_three=models.FileField(upload_to='imagefiles',
                                         blank=True,
                                         help_text="another image for the product")
    quantity=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    categories=models.ManyToManyField(Category)
    
    class Meta:
        db_table="products"
        ordering=['-created_at']
        
    def __unicode__(self):
        return self.product_name
    
    def get_abosolute_url(self):
        return reverse('product_slug', args=[self.product_slug])
    
    def sale_price():
        if self.old_price > price:
            return price
        
        else:
            return None
    
                                  
    