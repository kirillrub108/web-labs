# ЛР 17 · Класс Cart: метод __len__

> 274 · ЛР 17. Корзина · 9 из 34

**Зачем:** `len(cart)` — общее количество штук во всей корзине.

```python
class Cart(object):
    ...
    def __len__(self):                                     # общее количество штук
        return sum(item['quantity'] for item in self.cart.values())
```

---

← [273 · ЛР 17 · Класс Cart: метод __iter__](273_ЛР17_Класс-Cart-метод-__iter__.md) · [Оглавление](000_Оглавление.md) · [275 · ЛР 17 · Класс Cart: метод get_total_price](275_ЛР17_Класс-Cart-метод-get_total_price.md) →
