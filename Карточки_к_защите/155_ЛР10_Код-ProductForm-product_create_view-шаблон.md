# ЛР 10 · Код: ProductForm, product_create_view, шаблон

> 155 · ЛР 10. Форма создания записи · 3 из 16

```python
class ProductForm(forms.Form):
    title = forms.CharField(required=True, label="Название *",
                            widget=forms.TextInput(attrs={"placeholder": "Название продукта"}))
    description = forms.CharField(required=True, label="Описание *",
                            widget=forms.Textarea(attrs={"placeholder": "...", "rows": 5, "cols": 25}))
    ves = forms.CharField(required=True, label="Вес *")
```

```python
def product_create_view(request):
    form = ProductForm()                               # пустая форма
    if request.method == "POST":
        form = ProductForm(request.POST)               # форма с присланными данными
        if form.is_valid():                            # проверка
            Product.objects.create(**form.cleaned_data)   # запись в БД
    form = ProductForm()                               # очистка формы
    return render(request, "product/product_create.html", {"form": form})
```

```django
<form action="." method="POST"> {% csrf_token %}
    {{ form.as_p }}
    <input type='submit' value='Сохранить'/>
</form>
```

---

← [154 · ЛР 10 · Что сделано](154_ЛР10_Что-сделано.md) · [Оглавление](000_Оглавление.md) · [156 · ЛР 10 · Что такое форма Django и зачем она, если есть HTML `<form>`?](156_ЛР10_Что-такое-форма-Django-и-зачем-она-если-есть-HTML-form.md) →
