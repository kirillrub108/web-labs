# ЛР 13 · Код: LoanedProductByUserListView

> 207 · ЛР 13. Заказы пользователя · 3 из 13

```python
class LoanedProductByUserListView(LoginRequiredMixin, generic.ListView):
    model = ProductInstance
    template_name = 'product/productinstance_list_customer_user.html'
    paginate_by = 10

    def get_queryset(self):
        return ProductInstance.objects.filter(customer=self.request.user) \
                                      .filter(status_id__exact=2).order_by('due_back')
```

---

← [206 · ЛР 13 · Что сделано](206_ЛР13_Что-сделано.md) · [Оглавление](000_Оглавление.md) · [208 · ЛР 13 · Как связать заказ с пользователем?](208_ЛР13_Как-связать-заказ-с-пользователем.md) →
