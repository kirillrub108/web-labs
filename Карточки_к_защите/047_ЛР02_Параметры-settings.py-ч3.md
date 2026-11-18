# ЛР 2 · Параметры settings.py (3/3)

> 047 · ЛР 2. Настройки проекта (`settings.py`) · 5 из 16

| Параметр | Смысл | Значение у нас |
|---|---|---|
| `STATIC_URL`, `STATICFILES_DIRS` | статика (CSS, JS, картинки оформления) | `/static/`, `BASE_DIR/static` |
| `MEDIA_URL`, `MEDIA_ROOT` | загружаемые файлы (ЛР 16) | `/media/`, `BASE_DIR/media` |
| `CART_SESSION_ID` | наш собственный параметр — ключ корзины в сессии (ЛР 16) | `'cart'` |
| `LOGIN_REDIRECT_URL` | куда отправлять после входа (ЛР 12) | `'/'` |
| `MAILERS` | почтовый backend, сгенерирован `startproject` в Django 6.1; `console` — письма печатаются в консоль | не используется |

---

← [046 · ЛР 2 · Параметры settings.py (2/3)](046_ЛР02_Параметры-settings.py-ч2.md) · [Оглавление](000_Оглавление.md) · [048 · ЛР 2 · Зачем `BASE_DIR`?](048_ЛР02_Зачем-BASE_DIR.md) →
