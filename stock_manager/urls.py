from django.urls import path
from . import views

urlpatterns = [
    path('register_maker/', views.register_maker, name='register_maker'),
    path('maker_list/', views.maker_list, name='maker_list'),
    path('register_product/', views.register_product, name='register_product'),
    path('product_list/', views.product_list, name='product_list'),
    path('register_smartphone/', views.register_smartphone, name='register_smartphone'),
    path('smartphone_list/', views.smartphone_list, name='smartphone_list'),
    path('register_stock/', views.register_stock, name='register_stock'),
    path('stock_list/', views.stock_list, name='stock_list'),
]
