# ЛР 5 · История миграций products (1/2)

> 085 · ЛР 5. Изменение моделей · 3 из 16

**История миграций `products`:**

| № | Что делает | ЛР |
|---|---|---|
| 0001 | `CreateModel` Product (id, title, description) | 4 |
| 0002 | `AlterModelOptions` (verbose_name), `AlterField` title → CharField, description → null/blank | 4–5 |
| 0003 | `AddField` ves | 5 |
| 0004 | `AlterField` ×3 — добавлен `verbose_name` | 5 |
| 0005 | `CreateModel` Company + `AddField` product.company (FK) | 6 |

---

← [084 · ЛР 5 · Что сделано](084_ЛР05_Что-сделано.md) · [Оглавление](000_Оглавление.md) · [086 · ЛР 5 · История миграций products (2/2)](086_ЛР05_История-миграций-products-ч2.md) →
