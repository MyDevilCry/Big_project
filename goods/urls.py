from goods import views
from django.urls import path

app_name='catalog'

urlpatterns = [
     #Маємо два шляхи бо перший шлях вказує
    # на те що у нас ще буде сторінка після слагу
    path('search/', views.catalog,name='search'),
    path('<slug:category_slug>', views.catalog,name='index'),#Через slug передаємо написане транслітом ім'я
    path('product/<slug:product_slug>/', views.product,name='product'), #А тут вже передаємо ім'я продукту транслітом
    path('catalog/', views.catalog,name='catalog'),
    path('product/', views.product,name='product'),

]