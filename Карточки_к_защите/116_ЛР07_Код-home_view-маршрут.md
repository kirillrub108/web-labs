# ЛР 7 · Код: home_view, маршрут

> 116 · ЛР 7. Создание страниц сайта · 3 из 12

```python
def home_view(request, *args, **kwargs):
    print(args, kwargs)      # () {}
    print(request)           # <WSGIRequest: GET '/'>
    print(request.user)      # admin  или  AnonymousUser
    return render(request, "home.html", {})
```

```python
path('contact/', views.contact_view),
```

---

← [115 · ЛР 7 · Что сделано](115_ЛР07_Что-сделано.md) · [Оглавление](000_Оглавление.md) · [117 · ЛР 7 · Что такое представление (view)?](117_ЛР07_Что-такое-представление-view.md) →
