from django.urls import path
from . import views
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("products", views.ProductsView.as_view(), name="all-products"),
    path("products/<slug:slug>", views.ProductDetailView.as_view(), name="product-detail")
]
