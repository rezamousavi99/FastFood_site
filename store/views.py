from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Products
from django.utils.text import slugify
# Create your views here.


# class IndexView(View):
#
#     def get(self, request):
#         # list of newest product to oldest
#         sorted_products_list = list(Products.objects.all().order_by('-date'))
#         last_6_products = sorted_products_list[:6]
#         # print(last_6_products)
#         # print("**************", last_6_products[0].product_name)
#
#         return render(request, "store/index.html", {
#             "last_6_products": last_6_products
#         })
#
#     def post(self):
#         pass

class IndexView(ListView):
    template_name = "store/index.html"
    model = Products
    ordering = ["-date"]
    context_object_name = "last_6_products"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query[:6]
        return data

# class ProductsView(View):
#
#     def get(self, request):
#         all_products = Products.objects.all().order_by('-date')
#         return render(request, "store/all_products.html", {
#             "all_products": all_products
#         })

class ProductsView(ListView):
    template_name = "store/all_products.html"
    model = Products
    ordering = ["-date"]
    context_object_name = "all_products"


# class ProductDetailView(View):
#
#     def get(self, request, slug):
#         # all_product = Products.objects.all()
#         spc_product = get_object_or_404(Products, slug=slug)
#         print(spc_product.tags.all())
#         return render(request, "store/product_detail.html", {
#             "product": spc_product,
#             "product_tags": spc_product.tags.all()
#         })


class ProductDetailView(DetailView):
    template_name = "store/product_detail.html"
    model = Products
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        product_context = super().get_context_data()
        product_context["product_tags"] = self.object.tags.all()
        # product_context["product"] = self.object
        return product_context
