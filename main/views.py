from django.shortcuts import render
from goods.models import Categories

def index(request):

    categories = Categories.objects.all()


    context ={
        'title': 'home - Головна сторінка',
        'content': "Магазин меблів",
        'categories': categories
    }
    return render(request, "main/index.html", context)

def about(request):
    context ={
    'title': 'about - Про нас',
    'content': "Про нас",
    'text_on_page' : "Магазин крутий"}
    return render(request, "main/about.html",context)



