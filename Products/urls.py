from django.urls import path
from django.conf.urls import url
from . import views

app_name='Products'
urlpatterns=[
    path('', views.home_pageview, name='home_page'),
    path('products/',
        views.products_list, name='products_list'),
   url(r'^(?P<id>\d+)/(?P<product_slug>[-\w]+)/$',
        views.product_detail, name='product_detail'),
]