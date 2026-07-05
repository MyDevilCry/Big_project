from django.contrib import admin
from orders.models import Order, OrderItem

# admin.site.register(Order)
# admin.site.register(OrderItem)


class OrderItemTabularAdmin(admin.TabularInline):
    model = OrderItem
    fields = ('product','name', 'quantity', 'price')
    search_fields = ('product', 'name')
    extra = 0 # Це параметр який використовується для того щоб контролювати кількістю порожніх рядків для заповнення

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id','created_timestamp')
    search_fields = ('id','status','created_timestamp')

class OrderTabularAdmin(admin.TabularInline):
    model = Order
    fields = ("requires_delivery","status","payment_on_get","is_paid","created_timestamp")
    search_fields = ('requires_delivery','payment_on_get','status','created_timestamp')
    readonly_fields = ("created_timestamp",)
    extra = 0



