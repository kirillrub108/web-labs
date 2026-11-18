# ЛР 1 · Чем `django-admin` отличается от `manage.py`?

> 037 · ЛР 1. Установка ПО и создание проекта Django · 9 из 14

**Вопрос:** Чем `django-admin` отличается от `manage.py`?

**Ответ:** `django-admin` — общая утилита Django, доступна везде. `manage.py` — то же самое, но привязано к конкретному проекту: выставляет переменную `DJANGO_SETTINGS_MODULE=WebApp1.settings`. Поэтому после создания проекта пользуемся `python manage.py ...`.

---

← [036 · ЛР 1 · Что делает `django-admin startproject WebApp1`?](036_ЛР01_Что-делает-django-admin-startproject-WebApp1.md) · [Оглавление](000_Оглавление.md) · [038 · ЛР 1 · Что делает `runserver`?](038_ЛР01_Что-делает-runserver.md) →
