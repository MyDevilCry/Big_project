from django.db import models
from django.urls import reverse

class Categories(models.Model):
    name = models.CharField("Назва",max_length=100, unique=True)
    slug = models.SlugField('url',max_length=150, unique=True, blank=True, null=True)

    class Meta:
        db_table: str = "category"
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"
    def __str__(self):
        return self.name

class Products(models.Model):
    name = models.CharField("Назва", max_length=100, unique=True)
    slug = models.SlugField('url', max_length=150, unique=True, blank=True, null=True)
    description= models.TextField("Опис",blank=True, null=True)
    image = models.ImageField('Зображення' ,upload_to='goods_images',blank=True, null=True)
    price = models.DecimalField('Ціна',default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField('Знижка',default=0.00, max_digits=4, decimal_places=2)
    quantity = models.PositiveIntegerField('Кількість',default=0)
    category = models.ForeignKey(to=Categories,on_delete=models.PROTECT,verbose_name='Категорія')

    class Meta:
        db_table: str = "product"
        verbose_name= "Продукт"
        verbose_name_plural= "Продукти"
        ordering = ('id',)

    def __str__(self):
        return f'{self.name}, Кількість - {self.quantity}'

    def get_absolute_url(self):
        return reverse('catalog:product',kwargs={'product_slug':self.slug})

    def display_id(self): #Це ID товару записано
        return f' {self.pk:05}'

    def sell_price(self): #Це знижка
        if self.discount:
            return round (self.price - self.price * self.discount/100,2)
        return self.price

