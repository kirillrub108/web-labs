# ЛР 17 · Класс Cart: метод get_total_price

> 275 · ЛР 17. Корзина · 10 из 34

**Зачем:** общая стоимость корзины. Работает только после перебора корзины: цену в `Decimal` превращает `__iter__` (см. ловушку 10).

```python
class Cart(object):
    ...
    def get_total_price(self):                             # общая стоимость
        return sum(item['price'] * item['quantity'] for item in self.cart.values())
```

---

← [274 · ЛР 17 · Класс Cart: метод __len__](274_ЛР17_Класс-Cart-метод-__len__.md) · [Оглавление](000_Оглавление.md) · [276 · ЛР 17 · Класс Cart: метод clear](276_ЛР17_Класс-Cart-метод-clear.md) →
