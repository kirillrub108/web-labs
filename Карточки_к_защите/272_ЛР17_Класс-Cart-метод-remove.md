# ЛР 17 · Класс Cart: метод remove

> 272 · ЛР 17. Корзина · 7 из 34

**Зачем:** удалить позицию из корзины, если она там есть, и сохранить сессию.

```python
class Cart(object):
    ...
    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
```

---

← [271 · ЛР 17 · Класс Cart: метод save](271_ЛР17_Класс-Cart-метод-save.md) · [Оглавление](000_Оглавление.md) · [273 · ЛР 17 · Класс Cart: метод __iter__](273_ЛР17_Класс-Cart-метод-__iter__.md) →
