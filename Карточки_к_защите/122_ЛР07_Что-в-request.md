# ЛР 7 · Что в `request`?

> 122 · ЛР 7. Создание страниц сайта · 9 из 12

**Вопрос:** Что в `request`?

**Ответ:** Объект `WSGIRequest` со всеми данными запроса: `request.method` (`'GET'`/`'POST'`), `request.GET`, `request.POST` (данные формы), `request.user` (кто отправил), `request.session` (сессия), `request.path` (путь), `request.FILES`, `request.COOKIES`.

---

← [121 · ЛР 7 · Почему была ошибка 404 на `/home_view/`?](121_ЛР07_Почему-была-ошибка-404-на-home_view.md) · [Оглавление](000_Оглавление.md) · [123 · ЛР 7 · Зачем `*args, **kwargs`? Почему они пустые?](123_ЛР07_Зачем-args-kwargs-Почему-они-пустые.md) →
