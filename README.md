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
python manage.py runserver
```

Если `Activate.ps1` блокируется политикой выполнения, один раз выполните:
`Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

## Адреса

- Сайт: http://127.0.0.1:8000/
- Админка: http://127.0.0.1:8000/admin/ (логин и пароль из `createsuperuser`)

База (`db.sqlite3`) в git не хранится и после `migrate` пустая — компании и товары добавьте через админку или страницу `/create/`.

## Повторный запуск

```powershell
pythonproject\venv\Scripts\Activate.ps1
cd pythonproject\venv\Django\testproject\WebApp1
python manage.py runserver
```

Остановить сервер: `Ctrl+C`, выйти из окружения: `deactivate`.
