from distutils.command.upload import upload
from email.mime import image
from operator import truediv
from random import choices, randint
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
import random

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50,blank=False, null=False)
    image = models.ImageField(upload_to='cetagory',null=True , blank = True)
    parent = models.ForeignKey('self',blank=True, on_delete=models.CASCADE, null=True ,related_name='children')
    created=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name

class Meta:
    ordering=['-created']
    verbose_name_plural='Categories'
    
    
class Product(models.Model):
    name = models.CharField(max_length=200,blank=False, null=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    Pre_view_des = models.TextField(max_length=200,verbose_name='Short description')
    description = models.TextField(max_length=1000,verbose_name='Description')
    image = models.ImageField(upload_to='product',blank=False, null=False)
    price = models.FloatField()
    old_price = models.FloatField(default='0.00',blank=True, null=True)
    In_stoke = models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    
 
    def __str__(self):
        return self.name

    class Meta:
        ordering= ['-created']  
        
    
    def get_absolute_url(self):
        return reverse('product_details', kwargs={'slug': self.slug})
    
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_gellary')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.product.name)
    

class VariationManager(models.Manager):
    def sizes(self):
        return super(VariationManager, self).filter(variation='size')
    def colors(self):
        return super(VariationManager, self).filter(variation='color')

VARIATIONS_TYPE = (
    ( 'size','size'),
    ('color','color'),
)

class Product_variationValue(models.Model):
    variation = models.CharField(max_length=100, choices=VARIATIONS_TYPE)
    name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    
    objects = VariationManager()

    def __str__(self):
        return self.name

class BannerImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='banners')
    is_active = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name


