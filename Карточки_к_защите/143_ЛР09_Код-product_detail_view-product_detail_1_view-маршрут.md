# ЛР 9 · Код: product_detail_view, product_detail_1_view, маршрут, шаблон

> 143 · ЛР 9. Рендеринг данных из БД · 3 из 12

```python
def product_detail_view(request):
    obj = Product.objects.all()                # все записи
    return render(request, "product/detail.html", {"my_obj": obj})

def product_detail_1_view(request, id):        # id приходит из URL
    obj_1 = Product.objects.get(id=id)         # одна запись
    return render(request, "product/detail_product.html", {"my_obj_1": obj_1})
```

```python
path('detail_product/<int:id>', product_detail_1_view),
```

```django
<td>{{ i.description|truncatechars:9 }}</td>
<td><a href="/detail_product/{{ i.id }}">Подробнее о продукте</a></td>
```

---

← [142 · ЛР 9 · Что сделано](142_ЛР09_Что-сделано.md) · [Оглавление](000_Оглавление.md) · [144 · ЛР 9 · Что такое `Product.objects`?](144_ЛР09_Что-такое-Product.objects.md) →
