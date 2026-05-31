from django import forms
from django.contrib.auth.forms import AuthenticationForm



#forms.model.Form дозволяє РЕДАГУВАТИ вже готові дані
#attrs потрібен для того, щоб передати звичайні HTML-атрибути (такі як class, placeholder, id, тощо) з твого Python-коду прямо всередину HTML-тегу, який згенерує Django.
class UserLoginForm(AuthenticationForm): #Вона бере те, що ввів користувач, сама звіряє це з базою даних і каже, правильні дані чи ні.
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя','id': 'username'})
    )
    password = (forms.CharField
        (widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш пароль','id': 'password'})
    ))
