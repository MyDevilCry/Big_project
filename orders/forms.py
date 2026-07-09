import re

from django import forms

class CreateOrderForm(forms.Form):

    first_name = forms.CharField()
    last_name = forms.CharField()
    phone_number = forms.CharField()
    requires_delivery = forms.ChoiceField(
         choices=[
            ("0", False),
             ("1", True),
         ],)
    delivery_address = forms.CharField(required=False)
    payment_on_get = forms.ChoiceField(widget=forms.RadioSelect(),
         choices=[
             ("0", 'False'),
             ("1", 'True'),
        ],
     )
# Робимо валідацію для перевірки номеру телефона
    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        if not data.isdigit():
            raise forms.ValidationError("Номер должен содержать только цифры")

        pattern = re.compile(r"^\d{10}$") #Вказуємо те що номер телефону має містить 10 цифр
        if not pattern.match(data): #Перевіряємо паттерн якщо цифр менше видаємо користувачу помилку
            raise forms.ValidationError("Неверный формат номера")

        return data

    # first_name = forms.CharField(
    #     widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'placeholder': "Введите ваше имя"}
    #     )
    # )
    #
    # last_name = forms.CharField(
    #     widget=forms.TextInput(
    #     attrs={'class':'form-control','placeholder':"Введите вашу фамилию"}
    #     )
    # )
    #
    # phone_number = forms.CharField(
    #     widget=forms.TextInput(
    #     attrs={'class':'form-control','placeholder':"Введите ваш номер телефона"}
    #     )
    # )
    #
    # requires_delivery = forms.ChoiceField(
    #     widget=forms.RadioSelect(), #RadioSelect геренує кнопки на які може клікати користувач
    #     choices=[
    #         ("0", False),
    #         ("1", True),
    #     ],
    #     initial=0, #Цей параметр задає за замовченням активну кнопку коли користувач відкрив сайт
    # )
    #
    # delivery_address = forms.CharField(
    #     widget=forms.Textarea(
    #         attrs={'class':'form-control', id:'delivery_address', "rows":2 ,'placeholder':"Введите адрес доставки"}
    #     ),
    # required=False,
    # )
    #
    # payment_on_get = forms.ChoiceField(
    #     widget=forms.RadioSelect(),
    #     choices=[
    #         ("0", 'False'),
    #         ("1", 'True'),
    #     ],
    #     initial="card",
    # )