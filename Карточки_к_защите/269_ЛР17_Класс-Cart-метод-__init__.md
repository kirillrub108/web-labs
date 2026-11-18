# ЛР 17 · Класс Cart: метод __init__

> 269 · ЛР 17. Корзина · 4 из 34

**Зачем:** создать объект корзины для текущего запроса — достать корзину из сессии или положить туда пустой словарь.

```python
class Cart(object):
    ...
    def __init__(self, request):
        self.session = request.session                     # запомнили сессию
        cart = self.session.get(settings.CART_SESSION_ID)  # пробуем достать корзину
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}   # нет — создаём пустую
        self.cart = cart
```

---

← [268 · ЛР 17 · Как корзина выглядит в сессии](268_ЛР17_Как-корзина-выглядит-в-сессии.md) · [Оглавление](000_Оглавление.md) · [270 · ЛР 17 · Класс Cart: метод add](270_ЛР17_Класс-Cart-метод-add.md) →
