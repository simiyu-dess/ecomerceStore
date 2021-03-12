from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify


class Category(models.Model):
    category_name=models.TextField()
    category_id=models.IntegerField(auto_created=True)
    category_description=models.CharField(max_length=100)
    category_slug = models.SlugField(unique=True, max_length=255)
    meta_keywords = models.CharField("Meta Keywords", max_length=255,
                                help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField( "Meta Description", max_length=255, 
                                help_text='Content for description meta tag')    
    created_at = models.DateTimeField(auto_now_add=True)     
    updated_at = models.DateTimeField(auto_now=True)
    
    
    class meta:
        db_table="categories"
        ordering=['-created_at']
        verbose_name="category"
        verbose_name_plural="categories"
        
    def __unicode__(self):
        return self.category_name
    
    def __str__(self):
        return self.category_name
    
    def get_absolute_url(self):
        return reverse('Products:products_list_by_category', args=[self.category_slug])
# Create your models here.
