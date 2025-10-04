from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class Userprofile(AbstractUser):
    age = models.PositiveIntegerField(validators=[MinValueValidator(15),MaxValueValidator(70)],null=True,blank=True)
    phone_number = PhoneNumberField()
    STATUS_CHOICES = (
        ('gold', 'gold'), #75%
        ('sitve', 'silver'), #50%
        ('bronze"', 'bronze'),#25%py
        ('siple', 'siple')) #0%
    status = models.CharField(max_length=32, choices=STATUS_CHOICES, default='simple')
    created_data = models.DateTimeField(auto_created=True)

    def __str__(self):
        return f'{self.first_name}-{self.last_name}'

class Category(models.Model):
    category_image = models.ImageField(upload_to='category_image/')
    category_name = models.CharField(max_length=64, unique=True)


class SubCategory(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory_name = models.CharField(max_length=64,unique=True)


class Product (models.Model):
    subcategory = models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    product_name= models.CharField(max_length=56)
    price = models.PositiveSmallIntegerField()
    article_number = models.PositiveSmallIntegerField(unique=True)
    descriptions = models.TextField()
    video = models.FileField(upload_to= 'videos/',null=True, blank=True)


class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')


class Review(models.Model):
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField()
    stars = models.CharField(choices=[(i, str(i)) for i in range(1, 6)])


class Cart(models.Model):
    user = models.OneToOneField(Userprofile, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)
