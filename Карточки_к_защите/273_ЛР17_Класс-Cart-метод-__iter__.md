# ЛР 17 · Класс Cart: метод __iter__

> 273 · ЛР 17. Корзина · 8 из 34

**Зачем:** чтобы в шаблоне работал `{% for item in cart %}`. Одним запросом достаёт позиции из БД, считает сумму по каждой и отдаёт элементы по одному (`yield`).

```python
class Cart(object):
    ...
    def __iter__(self):                                    # для {% for item in cart %}
        product_ids = self.cart.keys()
        productss = Pozition_Price.objects.filter(id__in=product_ids)   # один запрос на все
        for product in productss:
            self.cart[str(product.id)]['product'] = product
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
```

---

← [272 · ЛР 17 · Класс Cart: метод remove](272_ЛР17_Класс-Cart-метод-remove.md) · [Оглавление](000_Оглавление.md) · [274 · ЛР 17 · Класс Cart: метод __len__](274_ЛР17_Класс-Cart-метод-__len__.md) →
