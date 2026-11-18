# ЛР 11 · Код: index_view

> 171 · ЛР 11. Bootstrap, редактирование и удаление, класс-представление · 3 из 21

```python
def index_view(request):
    num_product = Product.objects.all().count()
    num_company = Company.objects.all().count()
    num_instance = ProductInstance.objects.all().count()
    num_instance_available = ProductInstance.objects.filter(status_id__exact=2).count()
    ...
```

---

← [170 · ЛР 11 · Что сделано](170_ЛР11_Что-сделано.md) · [Оглавление](000_Оглавление.md) · [172 · ЛР 11 · Код: CompanyView](172_ЛР11_Код-CompanyView.md) →
