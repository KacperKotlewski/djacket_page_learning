from django.urls import path, include

from .views import LastestProduct, ProductDetail, CategoryDetail, search

urlpatterns = [
    path('latest-products/', LastestProduct.as_view()),
    path('products/search/', search),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
    path('products/<slug:category_slug>/', CategoryDetail.as_view()),
]
