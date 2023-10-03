from django.contrib import admin
from .models import Donate, Registration

@admin.register(Donate)
class DonateAdmin(admin.ModelAdmin):
    list_display=['name', 'amount', 'email']

