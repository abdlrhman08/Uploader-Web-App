from django.contrib import admin
from .models import Accounts, Payments

# Register your models here.
admin.site.register(Accounts)
admin.site.register(Payments)
