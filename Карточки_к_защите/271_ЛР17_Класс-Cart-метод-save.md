# ЛР 17 · Класс Cart: метод save

> 271 · ЛР 17. Корзина · 6 из 34

**Зачем:** записать корзину в сессию и выставить `modified = True` — иначе Django не заметит изменение вложенного словаря.

```python
class Cart(object):
    ...
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True                       # «сессия изменилась, сохрани»
```

---

← [270 · ЛР 17 · Класс Cart: метод add](270_ЛР17_Класс-Cart-метод-add.md) · [Оглавление](000_Оглавление.md) · [272 · ЛР 17 · Класс Cart: метод remove](272_ЛР17_Класс-Cart-метод-remove.md) →
