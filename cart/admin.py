from django.contrib import admin

from cart.models import Cart

#admin.site.register(Cart)

class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = ["product","quantity","created_timestamp"]
    search_fields = ["product","quantity","created_timestamp"]
    readonly_fields = ["created_timestamp"]
    extra = 1

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=["user_display","product","quantity","created_timestamp"]
    list_filter=["user","product__name","created_timestamp"]

#Робимо функціонал для адмінки
    def user_display(self,obj):
        if obj.user: #Ця строчка перевіряє чи є у кошика власник
            return str(obj.user) #Якщо кошик є то введи ім'я кошика
        return "Анонимный пользователь"

    def product_name(self,obj):
        return str(obj.product.name)
