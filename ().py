# coding: utf-8
x[0].name
x[1].description
x[0].description
x = Products.objects.filter(Q(name__contains="двухспальная") | Q(description__contains="двухспальная"))
from django.db.models import Q
from goods.utils import q_search
from goods.models import Products
x = Products.objects.filter(Q(name__contains="кровать") | Q(description__contains="кровать"))
x[0].name
