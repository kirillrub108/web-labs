# ЛР 11 · Код: product_delete_view

> 173 · ЛР 11. Bootstrap, редактирование и удаление, класс-представление · 5 из 21

```python
def product_delete_view(request, id):
    obj_2 = Product.objects.get(id=id)
    obj_2.delete()
    return redirect(reverse('product_detail'))
```

---

← [172 · ЛР 11 · Код: CompanyView](172_ЛР11_Код-CompanyView.md) · [Оглавление](000_Оглавление.md) · [174 · ЛР 11 · Код: product_edit_view](174_ЛР11_Код-product_edit_view.md) →
