from django.http import HttpResponseRedirect
from django.shortcuts import render,reverse

from cart.models import Cart
from users.forms import UserLoginForm, UserRegisterForm,ProfileForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect





def login(request):
    if request.method == 'POST': #Отримуємо метод пост від логіну
        form = UserLoginForm(request, data=request.POST) # request — для безпеки сесії, data=request.POST — звідки брати логін і пароль.
        if form.is_valid():
            user=form.get_user() #строчка повертає тобі вже готовий об'єкт користувача з бази даних, якого вона щойно успішно знайшла та перевірила
            auth.login(request,user) #ця строчка офіційно «впускає» користувача в систему і змушує сайт його запам'ятати.

            session_key = request.session.session_key

            messages.success(request,f"{form.cleaned_data['username']},Вы вошли в аккаунт")

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)


            if request.POST.get('next',None): #Цим кодом ми кажемо щоб get знайшов його значення якщо воно є, а якщо нема, нічого не відбудеться
                redirect_page = request.POST.get('next') or request.GET.get('next')
                if redirect_page and redirect_page != reverse('user:logout'): #сторінка редіректу дорівнює запиту який шукає Next або реквест отримує GET запит якщо такий є то він також видає next
                    return HttpResponseRedirect(request.POST.get('next'))

            return HttpResponseRedirect(reverse('main:index'))
    else :
            form = UserLoginForm()
    context = {     #Цей рядок потрібен для того щоб передати дані з views всередину  до HTML
            'title': 'home - Авторизация',
            'form' : form
        }
    return render(request, 'users/login.html',context)

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            session_key = request.session.session_key
            user= form.instance #Це потрібно для того щоб після реєстрації користувач уже став залогінений на сайті
            auth.login(request,user)

            messages.success(request, f"{form.cleaned_data['username']},Вы успешно зарегистрировались")

            if session_key:
                Cart.objects.filter(session_key=session_key).update(user=user)

            return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserRegisterForm()

    context = {
            'title': 'home - Авторизация',
            'form' : form
        }
    return render(request, 'users/registration.html',context)

def user_cart(request):
    return render(request,'users/users_cart.html')

@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user:profile'))
    else:
        form = ProfileForm(instance=request.user)

    context = {
        'title': 'Home - Кабинет',
        'form': form,
    }
    return render(request, 'users/profile.html',context)

def logout(request):
    messages.success(request, f"{request.user.username},Вы вышли из аккаунта")
    auth.logout(request)
    return redirect(reverse('main:index'))
