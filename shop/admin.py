from django.contrib import admin
from .models import User, Product, Cart, Coupone

# Register your models here.

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Coupone)
