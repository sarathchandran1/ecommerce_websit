from django.contrib import admin
from orders.models import order,orderd_Item
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_filter = [
        'owner',
        'order_status',
    ]
    search_fields = [
        'owner',
        'id',
    ]


admin.site.register(order,OrderAdmin)