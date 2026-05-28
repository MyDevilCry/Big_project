from goods.models import Products
from django.contrib.postgres.search import SearchVector, SearchQuery,SearchRank,SearchHeadline



def q_search(query):
    if query.isdigit() and len(query) <= 5: #Тут задаємо довжину символів
        return Products.objects.filter(id=int(query)) #Цей ретьорн повертає нам вже об'єкти по пошуку
    vector = SearchVector('name','description') #Вектор це направлення по якому пошук має знаходити товари
    query = SearchQuery(query)


    result = Products.objects.annotate(rank=SearchRank(vector,query)).filter(rank__gt=0).order_by('-rank')#Таким чином ми додаємо розумний пошук

    result = result.annotate( #Тут додаємо
        headline=SearchHeadline(
        'name',
        query,
        start_sel='<span style="background-color:yellow;">',
        stop_sel="</span>",
        )
    )
    result = result.annotate(
        bodyline=SearchHeadline(
        'description',
        query,
        start_sel='<span style="background-color:yellow;">',
        stop_sel="</span>",
        )
    )
    return result
