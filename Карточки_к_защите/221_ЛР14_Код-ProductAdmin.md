# ЛР 14 · Код: ProductAdmin

> 221 · ЛР 14. Настройка админ-панели · 4 из 15

```python
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'ves', 'company', 'show_count')
    list_filter = ('company',)
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductInstanceInline]
    search_fields = ("title__startswith",)

    def show_count(self, obj):
        from django.db.models import Count
        result = ProductInstance.objects.filter(product=obj).aggregate(Count('product'))
        return result["product__count"]
    show_count.short_description = "Количество,шт"

admin.site.register(Product, ProductAdmin)
```

---

← [220 · ЛР 14 · Код: ProductInstanceInline](220_ЛР14_Код-ProductInstanceInline.md) · [Оглавление](000_Оглавление.md) · [222 · ЛР 14 · Атрибуты ModelAdmin](222_ЛР14_Атрибуты-ModelAdmin.md) →
