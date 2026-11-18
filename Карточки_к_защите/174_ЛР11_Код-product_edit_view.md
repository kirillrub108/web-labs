# ЛР 11 · Код: product_edit_view

> 174 · ЛР 11. Bootstrap, редактирование и удаление, класс-представление · 6 из 21

```python
def product_edit_view(request, id):
    get_product = Product.objects.get(id=id)
    if request.method == 'POST':
        get_product.title = request.POST.get('title')
        ...
        get_product.save()
        return HttpResponseRedirect("/detail")
    else:
        return render(request, "product/edit_product.html", {'get_product': get_product})
```

---

← [173 · ЛР 11 · Код: product_delete_view](173_ЛР11_Код-product_delete_view.md) · [Оглавление](000_Оглавление.md) · [175 · ЛР 11 · Что такое Bootstrap и как подключён?](175_ЛР11_Что-такое-Bootstrap-и-как-подключён.md) →
