from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,User
#forms.model.Form дозволяє РЕДАГУВАТИ вже готові дані
#attrs потрібен для того, щоб передати звичайні HTML-атрибути (такі як class, placeholder, id, тощо) з твого Python-коду прямо всередину HTML-тегу, який згенерує Django.
class UserLoginForm(AuthenticationForm): #Наслідуємо спеціальну форму аутентифікації
    username = forms.CharField(
        label = 'Имя',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваше имя пользователя','id': 'username'}),
    )
    password = forms.CharField(
        label = 'Пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш пароль','id': 'password'})
    )

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'first_name',
                  'last_name',
        )


