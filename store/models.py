from django.db import models
from django.urls import reverse


# Create your models here.


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name
    

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class Tag(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption


class Products(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    Description = models.TextField()
    date = models.DateField(auto_now=True)
    image = models.CharField(max_length=100, null=True)
    slug = models.SlugField(unique=True, db_index=True, null=True)
    tags = models.ManyToManyField(Tag)
    # tags = models.

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return f'{self.product_name} {self.price}'

    def get_absolute_url(self):
        return reverse("product-detail", kwargs={"slug": self.slug})


class OrderMaster(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    # doubt
    status = models.BooleanField()
    address = models.TextField(null=True)

    def __str__(self):
        return f"{self.date} ({self.time:%H:%M}) - {self.customer}"
    

# def get_price(x):
#     price = Products.objects.get(product_name=x).price
#     return price


class OrderDetails(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    order_master = models.ForeignKey(OrderMaster, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    pure_price = models.IntegerField()
    # pure_price = models.GeneratedField(
    #     expression=Products.objects.get(product_name=product).price,
    #     output_field=models.IntegerField(),
    #     db_persist=True
    # )
    total_price = models.IntegerField()

    class Meta:
        verbose_name_plural = "Order details"

    def __str__(self):
        return f'{self.product} ({self.quantity})'
    
    # def save(self, *args, **kwargs):
    #     self.pure_price = get_price(self.product)
    #     super().save(*args, **kwargs)