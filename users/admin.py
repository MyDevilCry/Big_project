from django.contrib import admin

from cart.admin import CartTabAdmin
from .models import User

#admin.site.register(User) #Як реєстрували адміна так і реєструємо користувача

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=["username","first_name","last_name","is_staff","is_superuser","email"]
    search_fields = ["username","first_name","last_name","email"]

    inlines = [CartTabAdmin,]