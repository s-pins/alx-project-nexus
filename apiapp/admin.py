from django.contrib import admin
from .models import Cart, CartItem, CustomUser, Category, Order, OrderItem, Product, ProductRating, Review, Wishlist
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name')
    search_fields = ('email', 'username', 'first_name', 'last_name')
admin.site.register(CustomUser, CustomUserAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'featured', 'category')
    search_fields = ('name', 'description')
    list_filter = ('featured', 'category')
admin.site.register(Product, ProductAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
admin.site.register(Category, CategoryAdmin)


admin.site.register([Cart, CartItem, Review, ProductRating, Wishlist, Order, OrderItem])