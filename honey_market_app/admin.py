from django.contrib import admin
from .models import Product, Order, OrderItem, Mesaj

# inregistrare modele gestionate din interfata Django admin
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Mesaj)