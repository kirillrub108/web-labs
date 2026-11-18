# ЛР 17 · Почему цена хранится строкой `str(product.cost_product)`?

> 284 · ЛР 17. Корзина · 19 из 34

**Вопрос:** Почему цена хранится строкой `str(product.cost_product)`?

**Ответ:** Цена — `Decimal`, а JSON не умеет сериализовать `Decimal` (ошибка «Object of type Decimal is not JSON serializable»). Сохраняем строкой, а при выводе превращаем обратно: `Decimal(item['price'])`.

---

← [283 · ЛР 17 · Почему ключ — строка `str(product.id)`?](283_ЛР17_Почему-ключ-строка-strproduct.id.md) · [Оглавление](000_Оглавление.md) · [285 · ЛР 17 · Зачем `self.session.modified = True`?](285_ЛР17_Зачем-self.session.modified-True.md) →
