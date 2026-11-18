# ЛР 15 · Код: RegistrForm, registrat

> 235 · ЛР 15. Регистрация пользователя · 3 из 14

```python
class RegistrForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Поле обязательное для заполнения')
    first_name = forms.CharField(required=True, label="Ваше имя", max_length=254)
    last_name = forms.CharField(required=True, label="Ваша фамилия", max_length=254)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2',)
```

```python
def registrat(request):
    data = {}
    if request.method == 'POST':
        form = RegistrForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            data['form'] = form
            return render(request, 'registration/registration_out.html', data)
    else:
        form = RegistrForm()
        data['form'] = form
    return render(request, 'registration/registration.html', data)
```

---

← [234 · ЛР 15 · Что сделано](234_ЛР15_Что-сделано.md) · [Оглавление](000_Оглавление.md) · [236 · ЛР 15 · Что такое `UserCreationForm`?](236_ЛР15_Что-такое-UserCreationForm.md) →
