from django.urls import path
from django.conf.urls import url, re_path
from . import views

app_name='Products'
urlpatterns=[
    path('', views.home_pageview, name='home_page'),
    re_path(r'^(?P<id>\d+)/(?P<product_slug>[-\w]+)/$',
        views.product_detail, name='product_detail'),
    re_path(r'^(?P<category_slug>[-\w]+)/$',
        views.products_list, name='products_list_by_category'),
    re_path(r'^(?P<brand_slug>[-\w]+)/$',
        views.products_list_by_brand_view, name='products_list_by_brand'),
]