from django.contrib import admin
from .models import  *
from .models import  Product




admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Client)
admin.site.register(ShopCart)
admin.site.register(Order)
