from django.http import JsonResponse
from django.template.loader import render_to_string
from cart.templatetags.utils import  get_user_cart



from cart.models import Cart
from goods.models import Products



def cart_add(request):
    product_id = request.POST.get("product_id")
    product = Products.objects.get(id=product_id) # Цей рядок потрібен для того щоб заглянути в базу даних і побачити чи є там товар
    if not request.session.session_key: #Додаємо цей код для перевірки що користувач неавторізований
        request.session.create()
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user,product=product)
        #дивиться на всю таблицю кошиків. #відсікає кошики всіх інших людей і дивиться тільки на товари цього конкретного користувача.
        if carts.exists():
            cart = carts.first() #Ця строка працює з даними які лежать в списку carts
            cart.quantity += 1 # Додаємо товар у кошик
            cart.save()
        else :
            Cart.objects.create(user=request.user,product=product,quantity=1) #В іншому випадку додаємо товар у кошик користувача вперше

    else :
        Cart.objects.filter(session_key=request.session.session_key, product=product) #Робимо карту для неавторизованого користувача
        carts = Cart.objects.filter(session_key=request.session.session_key, product=product)
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(session_key=request.session.session_key,product=product,quantity=1)

    user_carts = get_user_cart(request)
    cart_items_html = render_to_string("cart/includes/included_cart.html",{'carts':user_carts},request=request)

    response_data = {
        "message" : "Товар добавлен в корзину",
        "cart_items_html" : cart_items_html ,
    }
    return JsonResponse(response_data) #Робимо цей редірект щоб після додавання товару у кошик користувач залишався на тій самій сторінці

def cart_change(request):
    cart_id = request.POST.get("cart_id") #Дізнаємось id товару на який клікнув користувач
    quantity_item = request.POST.get("quantity") # Дізнаємось змінену кількість товару

    cart = Cart.objects.get(id=cart_id) #Отримуємо з бази даних конкретний елемент кошика за id

    cart.quantity = quantity_item
    cart.save()


    user_carts = get_user_cart(request)
    cart_items_html = render_to_string("cart/includes/included_cart.html",{'carts':user_carts},request=request)
    response_data = {
        "message": 'Количество изменено',
        "cart_items_html" : cart_items_html ,

    }
    return JsonResponse(response_data)

def cart_remove(request):
    cart_id = request.POST.get("cart_id")
    cart = Cart.objects.get(id=cart_id) #Дивимось у базу даних для кошика
    quantity = cart.quantity
    cart.delete()

    user_carts = get_user_cart(request)
    cart_items_html = render_to_string ("cart/includes/included_cart.html", {'carts':user_carts}, request=request)
    response_data = {
        "message": "Товар удалён ",
        "cart_items_html" : cart_items_html ,
        "quantity_deleted": quantity ,
    }
    return JsonResponse(response_data)
