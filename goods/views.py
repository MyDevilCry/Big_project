from goods.models import Products  # Додали імпорт тут
from django.shortcuts import render, get_list_or_404,redirect
from django.core.paginator import Paginator
from goods.utils import q_search



def catalog(request, category_slug=None):

 page=request.GET.get('page',1)#таким способом ми будемо передавати ту сторінку на яку ми клікаємо
 on_sale = request.GET.get('on_sale',None) #Ця фунція відповідає за фільтрацію
 order_by = request.GET.get('order_by',None) #Ця функція відповідає за порядок товарів
 query = request.GET.get('q',None)



 # Усі ці рядки МАЮТЬ мати відступ (4 пробіли або 1 Tab)

 if query:
  goods = q_search(query)
  if query.isdigit() and goods.exists() and goods.count() == 1:
     product = goods.first()
     return redirect('catalog:product',product_slug=product.slug)

 elif category_slug is None or category_slug.lower() == 'all':
  goods = Products.objects.all()

 else:
  goods = get_list_or_404 (Products.objects.filter(category__slug=category_slug)) #Get list для того щоб якщо браузер
  # отримує пусту сторінку без товарів то сайт видає помилку
  #Пагінатор динамічно підлаштовується під результат твого запиту в базу.
 if on_sale:
    goods = goods.filter(discount__gt=0) #те що у дужках вказує на те що ми фільтруємо товари по знижці
 if order_by and order_by != 'default':
    goods = goods.order_by(order_by)

 paginator = Paginator(goods, 6 ) #Тут я роблю те скільки товарів буде відображатись на сторінці
 current_page = paginator.get_page(page) #Це номер сторінки який я відображаю


 context = {
  "title": "Home - Каталог",
  "goods": current_page,
  "page_slug": category_slug,

 }
 return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
 product_item = Products.objects.get(slug=product_slug)

 context = {
  'product': product_item
 }

 return render(request, 'goods/product.html', context)

