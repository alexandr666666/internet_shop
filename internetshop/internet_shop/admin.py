from django.contrib import admin
from .models import Product, Account, Enter_code, Card_Number

admin.site.register(Product)
admin.site.register(Account)
admin.site.register(Enter_code)
admin.site.register(Card_Number)

