from django import template
from cart.models import Cart

register = template.Library()

@register.simple_tag()
def user_carts(request): #Робимо кошик для зареєстрованого користувача
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user)

    if not request.session.session_key: #А цей кошик не для зареєстрованого користувача
        request.session.save()
    return Cart.objects.filter(user=request.user)

