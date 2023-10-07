from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ['code','valid_from','valid_to','discount','active']
    list_filter = ['active','valid_from','valid_to']
    seacrh_fields = ['code']
    
