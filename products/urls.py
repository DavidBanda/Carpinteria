# from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='products-home'),
    path('about/', views.about, name='products-about'),
    path('productos/', views.ProductListView.as_view(), name='products-product_grid'),
    path('productos/<str:title>/<int:pk>/', views.productSingle.as_view(), name='product-single')
]