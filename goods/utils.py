from goods.models import Products
from django.db.models import Q

def q_search(query):
    if query.isdigit() and len(query) <= 5:
        return Products.objects.filter(id=int(query))
    keywords = [word for word in query.split() if len(word) > 2] #Це ключи для слів по яким буде пошук.
    q_objects = Q()

    for token in keywords: #Робимо умову для слова в цьому ключі де містить пошук
        q_objects |= Q(description__icontains=token) |Q (name__icontains=token) #Обов'язково ДОДАЄМО | для того щоб
        #джанго розумів що пошук має бути і за описом і за ім'ям
    return Products.objects.filter(q_objects)
