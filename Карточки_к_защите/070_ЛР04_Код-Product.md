# ЛР 4 · Код: Product

> 070 · ЛР 4. Создание приложения. Модели · 3 из 15

```python
class Product(models.Model):                      # наследование → это модель
    title = models.CharField(max_length=120, verbose_name="Название")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    ...
    def __str__(self):                            # как объект показывается текстом
        return self.title
    class Meta:                                   # метаданные модели
        verbose_name = "Продукт",
        verbose_name_plural = "Продукты"
```

---

← [069 · ЛР 4 · Что сделано](069_ЛР04_Что-сделано.md) · [Оглавление](000_Оглавление.md) · [071 · ЛР 4 · Что такое модель?](071_ЛР04_Что-такое-модель.md) →
