# ЛР 2 · Параметры settings.py (2/3)

> 046 · ЛР 2. Настройки проекта (`settings.py`) · 4 из 16

| Параметр | Смысл | Значение у нас |
|---|---|---|
| `ROOT_URLCONF` | главный файл маршрутов | `'WebApp1.urls'` |
| `TEMPLATES` | настройки шаблонизатора | `DIRS` = `BASE_DIR/templates` (ЛР 8) |
| `WSGI_APPLICATION` | точка входа для сервера | `'WebApp1.wsgi.application'` |
| `DATABASES` | подключение к БД | SQLite, файл `db.sqlite3` |
| `AUTH_PASSWORD_VALIDATORS` | проверки надёжности пароля | 4 валидатора |
| `LANGUAGE_CODE`, `TIME_ZONE`, `USE_I18N`, `USE_TZ` | язык, часовой пояс | `en-us`, `UTC` |

---

← [045 · ЛР 2 · Параметры settings.py (1/3)](045_ЛР02_Параметры-settings.py-ч1.md) · [Оглавление](000_Оглавление.md) · [047 · ЛР 2 · Параметры settings.py (3/3)](047_ЛР02_Параметры-settings.py-ч3.md) →
