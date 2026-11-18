# ЛР 17 · Класс Cart: метод add

> 270 · ЛР 17. Корзина · 5 из 34

**Зачем:** добавить позицию прайса или изменить её количество. Ключ — `str(id)`, цена — строкой: сессия хранится в JSON.

```python
class Cart(object):
    ...
    def add(self, product, quantity=1, update_quantity=False):
        product_id = str(product.id)                       # ключ — строка
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.cost_product)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity   # заменить количество
        else:
            self.cart[product_id]['quantity'] += quantity  # прибавить
        self.save()
```

---

← [269 · ЛР 17 · Класс Cart: метод __init__](269_ЛР17_Класс-Cart-метод-__init__.md) · [Оглавление](000_Оглавление.md) · [271 · ЛР 17 · Класс Cart: метод save](271_ЛР17_Класс-Cart-метод-save.md) →
