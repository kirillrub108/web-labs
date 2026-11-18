# Архитектура MVT (Model — View — Template)

> 014 · Теория с нуля · 1.3. Что такое Django

**Архитектура MVT (Model — View — Template):**

| Слой | Что делает | Где в проекте |
|---|---|---|
| **Model** | описывает данные и работу с БД | `products/models.py` |
| **View** | логика: получить запрос, взять данные, вернуть ответ | `*/views.py` |
| **Template** | внешний вид: HTML с подстановкой данных | `templates/*.html` |

Отличие от классического **MVC**: то, что в MVC называется Controller, в Django делит между собой сам фреймворк (диспетчер URL) и View; а Django-Template соответствует View из MVC.

---

← [013 · Django](013_Теория_Django.md) · [Оглавление](000_Оглавление.md) · [015 · ORM (Object-Relational Mapping)](015_Теория_ORM-Object-Relational-Mapping.md) →
