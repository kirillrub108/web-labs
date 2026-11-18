# ЛР 2 · Что такое middleware?

> 053 · ЛР 2. Настройки проекта (`settings.py`) · 11 из 16

**Вопрос:** Что такое middleware?

**Ответ:** Цепочка обработчиков, через которые проходит каждый запрос до представления и каждый ответ после. Наши: `SecurityMiddleware` (заголовки безопасности), `SessionMiddleware` (создаёт `request.session`), `CommonMiddleware` (в т.ч. дописывает слэш в конце URL), `CsrfViewMiddleware` (защита форм), `AuthenticationMiddleware` (создаёт `request.user`), `MessageMiddleware`, `XFrameOptionsMiddleware` (запрет встраивать сайт во фрейм — защита от кликджекинга). **Порядок важен:** `AuthenticationMiddleware` стоит после `SessionMiddleware`, потому что пользователь определяется по сессии.

---

← [052 · ЛР 2 · Что в `INSTALLED_APPS` по умолчанию?](052_ЛР02_Что-в-INSTALLED_APPS-по-умолчанию.md) · [Оглавление](000_Оглавление.md) · [054 · ЛР 2 · Как перейти на PostgreSQL/MySQL?](054_ЛР02_Как-перейти-на-PostgreSQLMySQL.md) →
