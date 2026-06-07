from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,get_user_model

User = get_user_model()
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


    def save(self, commit=True): #commit=True — це наказ. Він означає: "За замовчуванням, як тільки дані оброблені, відразу запиши їх у базу даних".
        user = super().save(commit=False) #Цим ми кажемо Django:
# "Візьми дані з форми (username, email, first_name, last_name), створи з них тимчасовий об'єкт користувача в пам'яті комп'ютера, але поки що не записуй його в базу даних".
        user.set_password(self.cleaned_data['password1']) #Тут ми робимо так щоб коли користувач ввів пароль, ця строка його зашифрувала
        if commit: #якщо я викликаю метод як form.save(), то commit автоматично дорівнює True
            user.save()








