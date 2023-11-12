from django.contrib import admin
from home.models import Product
from home.models import Cart
from home.models import Order
from home.models import CustomerProfile


# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(CustomerProfile)

