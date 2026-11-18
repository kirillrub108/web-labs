# ЛР 17 · Класс Cart: метод clear

> 276 · ЛР 17. Корзина · 11 из 34

**Зачем:** удалить корзину из сессии целиком (заготовка под оформление заказа, пока не используется).

```python
class Cart(object):
    ...
    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
```

---

← [275 · ЛР 17 · Класс Cart: метод get_total_price](275_ЛР17_Класс-Cart-метод-get_total_price.md) · [Оглавление](000_Оглавление.md) · [277 · ЛР 17 · Форма и представления](277_ЛР17_Форма-и-представления.md) →
