from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.IntegerField()
    desc = models.CharField(max_length=300)
    date = models.DateTimeField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=300)
    disc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='media/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name 

   
    
    def save(self, *args, **kwargs):
        # Automatically generate the slug based on the title
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    






    
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    image = models.ImageField(upload_to='media/')
    quantity = models.PositiveBigIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='orders')  # Correct the ForeignKey reference
    order_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=400)
    pincode = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order for {self.product.name} by {self.user.username}"



class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
       return self.user
