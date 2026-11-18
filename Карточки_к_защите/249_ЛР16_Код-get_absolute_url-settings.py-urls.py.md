# ЛР 16 · Код: get_absolute_url, settings.py, urls.py

> 249 · ЛР 16. Интернет-магазин: изображения, цены, сессии · 3 из 19

```python
slug = models.SlugField(max_length=200, db_index=True, allow_unicode=True, ...)
image = models.ImageField(upload_to='images/', blank=True, ...)

def get_absolute_url(self):
    return reverse('detail_product', args=[self.id])
```

```python
# settings.py
MEDIA_URL = '/media/'
MEDIA_ROOT = Path.joinpath(BASE_DIR, "media")
CART_SESSION_ID = 'cart'
```

```python
# urls.py
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

← [248 · ЛР 16 · Что сделано](248_ЛР16_Что-сделано.md) · [Оглавление](000_Оглавление.md) · [250 · ЛР 16 · Зачем Pillow?](250_ЛР16_Зачем-Pillow.md) →
