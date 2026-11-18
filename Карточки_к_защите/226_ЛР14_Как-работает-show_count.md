# ЛР 14 · Как работает `show_count`?

> 226 · ЛР 14. Настройка админ-панели · 9 из 15

**Вопрос:** Как работает `show_count`?

**Ответ:** Метод `ModelAdmin`, вызывается для каждой строки списка; `obj` — продукт этой строки. `filter(product=obj)` отбирает экземпляры продукта, `aggregate(Count('product'))` считает их на стороне БД и возвращает **словарь** `{'product__count': 2}`. `short_description` — заголовок столбца.

---

← [225 · ЛР 14 · Что такое inline? `TabularInline` vs `StackedInline`?](225_ЛР14_Что-такое-inline-TabularInline-vs-StackedInline.md) · [Оглавление](000_Оглавление.md) · [227 · ЛР 14 · `aggregate` vs `annotate`?](227_ЛР14_aggregate-vs-annotate.md) →
