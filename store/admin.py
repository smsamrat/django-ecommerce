from django.contrib import admin
from store.models import Category, Product, ProductImages, Product_variationValue

# Register your models here.
class PostImageAdmin(admin.StackedInline):
    model = ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]
    prepopulated_fields ={'slug': ('name',)}
    
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Product_variationValue)
