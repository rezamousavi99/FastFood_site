from django.contrib import admin
from . import models
# Register your models here.
from .models import Products


class OrderMasterAdmin(admin.ModelAdmin ):
    readonly_fields = ('date', 'time', )
    list_filter = ("date", "customer", )
    list_display = ("customer", "date", "time", )


class OrderDetailsAdmin(admin.ModelAdmin):
    list_filter = ("product", "order_master")
    list_display = ("product", "quantity", "order_master", "total_price", )


class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ("date", )
    list_filter = ("category", "tags", )
    list_display = ("product_name", "price", "category")
    prepopulated_fields = {"slug": ("product_name",)}


admin.site.register(models.Tag)
admin.site.register(models.Customer)
admin.site.register(models.Category)
admin.site.register(models.Products, ProductAdmin)
admin.site.register(models.OrderMaster, OrderMasterAdmin)
admin.site.register(models.OrderDetails, OrderDetailsAdmin)
admin.site.register(models.Comments)