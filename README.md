# WebApp1 — интернет-магазин на Django

Django 6.1.1 + SQLite. Нужен **Python 3.12+**.

Проект лежит в `pythonproject/venv/Django/testproject/WebApp1/`.

## Запуск (PowerShell)

```powershell
git clone <URL-репозитория> web-labs
cd web-labs

python -m venv pythonproject\venv
pythonproject\venv\Scripts\Activate.ps1
pip install -r requirements.txt

cd pythonproject\venv\Django\testproject\WebApp1
python manage.py migrate
python manage.py createsuperuser
python seed.py
python manage.py runserver
```

Если `Activate.ps1` блокируется политикой выполнения, один раз выполните:
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

## Адреса

- Сайт: http://127.0.0.1:8000/
- Админка: http://127.0.0.1:8000/admin/ (логин и пароль из `createsuperuser`)

## Данные из методички

База (`db.sqlite3`) в git не хранится и после `migrate` пустая. Данные, которые вносились по методичке (ЛР 4–17), восстанавливает скрипт `seed.py` (лежит рядом с `manage.py`). Запускать его нужно **после `createsuperuser`**: тогда суперпользователь получает `id=1`, а пользователи ниже — `id` 2–4, как в исходной базе.

`python seed.py` создаёт:

| Что | Содержимое |
|---|---|
| Компании | ООО «Канцтовары», ООО «Бумажный мир» |
| Продукты | id 1 «Карандаш простой HB», id 3 «Тетрадь», id 4 «Линейка» (с картинками из `media/images/`; `id=2` в методичке был удалён) |
| Статусы | 1 «На складе», 2 «В заказе», 3 «Продана» |
| Экземпляры | `1_1_1`, `1_1_2` (в заказе, Пользователь_2), `2_3_1` (в заказе, Пользователь_1), `2_3_2` |
| Прайс-лист | № 1 с ценами: карандаш 25, тетрадь 40, линейка 30 (по ним считается корзина) |
| Пользователи | `Пользователь_1` (персонал, группа «Пользователи сайта»), `Пользователь_2`, `Пользователь_3`; пароли указаны в начале `seed.py` |

Суперпользователя скрипт не создаёт и не меняет — используется тот, что создан `createsuperuser`. Скрипт можно запускать повторно: записи обновляются по `id`, пароли существующих пользователей не сбрасываются.

## Повторный запуск

```powershell
pythonproject\venv\Scripts\Activate.ps1
cd pythonproject\venv\Django\testproject\WebApp1
python manage.py runserver
```

Остановить сервер: `Ctrl+C`, выйти из окружения: `deactivate`.
