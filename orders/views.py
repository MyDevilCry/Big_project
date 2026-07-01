from django.db import transaction
from django.shortcuts import render,redirect
from django.forms import ValidationError
from orders.models import OrderItem
from django.contrib import messages

from cart.models import Cart

from orders.forms import CreateOrderForm
from orders.models import Order


def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic(): #Ця строка потрібна для безпеки у разі збою сайту, або інтернету користувача, воно відкатує назад замовлення
                    cart_items = Cart.objects.filter(user=request.user)
                    user=request.user
                    if cart_items.exists(): #Тут ми створюємо замовлення
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )

                        for cart_item in cart_items: #Запускаємо цикл по всіх елементах які лежать у кошику користувача
                            product = cart_item.product #Витягуємо об'єкт з кошика
                            name = cart_item.product.name #Беремо текстову назву товару
                            price = cart_item.product.sell_price
                            quantity = cart_item.quantity

                            if product.quantity < quantity: #Якщо продукту немає на складі , видаємо користувачу помилку
                                raise ValidationError(f" Недостаточное количество товара {name} на складе\ В наличии {product.quantity}")
                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity = quantity
                            product.save()

                        cart_items.delete() #Видаляємо товари з кошику після того як покупець зробив замовлення
                        messages.success(request,"Заказ оформлен!")
                        return redirect('user:profile')
            except ValidationError as e:
                messages.error(request, str(e)) # Через e передаємо користувачу помилку
                return redirect('cart:order')
    else:
        initial = { #створюємо це поле для того щоб користувач не вводив щоразу ім'я та прізвище
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
        }
        form = CreateOrderForm(initial=initial)
        context = {
            'title':'Home - оформление заказа',
            'form': form,
        }
    return render(request, 'orders/create_order.html',context=context)
