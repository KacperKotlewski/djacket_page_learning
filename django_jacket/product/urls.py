from django.urls import path, include

from .views import LastestProduct, ProductDetail

urlpatterns = [
    path('latest-products/', LastestProduct.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductDetail.as_view()),
]
