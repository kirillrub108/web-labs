from django import forms

from .models import Product

class ProductForm(forms.Form):
        title       = forms.CharField(required=True, label="Название *",widget=forms.TextInput(
                                                                   attrs={"placeholder":"Название продукта"}))
        description = forms.CharField(required=True, label="Описание *",
                                      widget=forms.Textarea(
                                          attrs={
                                          "placeholder":"Описание продукта",
                                          "rows":5,
                                          "cols":25
                                          }
                                           ))
        ves         = forms.CharField(required=True, label="Вес *")


# Подключение компонента UserCreationForm
from django.contrib.auth.forms import UserCreationForm
# Подключение модели User
from django.contrib.auth.models import User

#Создание класса формы
class RegistrForm(UserCreationForm):
  # Добавление новое поля Email
  email = forms.EmailField(max_length=254, help_text='Поле обязательное для заполнения')
  first_name=forms.CharField(required=True, label="Ваше имя",max_length=254)
  last_name=forms.CharField(required=True, label="Ваша фамилия",max_length=254)

  class Meta:
    # Свойство модели User
    model = User
    # Свойство назначения полей
    fields = ('first_name','last_name','email', 'username','password1', 'password2', )
