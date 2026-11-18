# ЛР 2 · Как перейти на PostgreSQL/MySQL?

> 054 · ЛР 2. Настройки проекта (`settings.py`) · 12 из 16

**Вопрос:** Как перейти на PostgreSQL/MySQL?

**Ответ:** Поменять в `DATABASES` `ENGINE` (`django.db.backends.postgresql`), указать `NAME`, `USER`, `PASSWORD`, `HOST`, `PORT`, поставить драйвер и выполнить `migrate`. Код моделей и представлений не меняется — в этом смысл ORM.

---

← [053 · ЛР 2 · Что такое middleware?](053_ЛР02_Что-такое-middleware.md) · [Оглавление](000_Оглавление.md) · [055 · ЛР 2 · Почему SQLite?](055_ЛР02_Почему-SQLite.md) →
