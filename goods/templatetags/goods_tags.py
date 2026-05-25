from goods.models import Categories
from django import template
from django.utils.http import urlencode

register = template.Library()
@register.simple_tag() #Реєстрація для того щоб я міг взаємодіяти з функцією де завгодно
def tag_categories(): #Функція повертає каталог коли ми у якомусь розділі
    return Categories.objects.all()

#Цей кастомний тег шаблону Django потрібен для вирішення проблем з фільтрами та пагінацією
# — для збереження поточних параметрів URL-адреси при переході на іншу сторінку.
# Пам'ятка для себе, kwargs це по суті ключ який поглинає в себе кількість параметрів,яку я передаю у тег з HTML-шаблону, і перетворює їх на словник.
@register.simple_tag(takes_context=True)
def change_params(context,**kwargs):
    query = context['request'].GET.dict() #query служить звичайним Python-словником , який тимчасово зберігає всі шматочки адресного рядка (URL-параметри).
    query.update(kwargs) # update бере нові значення з kwargs (ті, що я передаєю у тег всередині HTML) і додає їх до нашого query
    return urlencode (query)



