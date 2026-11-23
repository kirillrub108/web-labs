"""Заполнение БД данными, которые вносились по методичке (ЛР 6-16).

Запуск из папки с manage.py, после `python manage.py migrate`:
    python seed.py

Повторный запуск безопасен: записи обновляются по id, пароли уже
существующих пользователей не меняются. Суперпользователя скрипт не
создаёт и не трогает - он создаётся командой createsuperuser (ЛР 3).
"""
import os
from datetime import date

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WebApp1.settings")
django.setup()

from django.contrib.auth.models import Group, User
from products.models import (Company, Pozition_Price, Price, Product,
                             ProductInstance, Status)

# --- пользователи сайта (ЛР 12, 13, 15) ---------------------------------
# логин, пароль, имя, фамилия, e-mail, статус персонала
USERS = [
    ("Пользователь_1", "usr1_4827", "Тестовый", "Пользователь", "", True),
    ("Пользователь_2", "usr2_6153", "Тестовый", "Покупатель", "", False),
    ("Пользователь_3", "reg3_5914Kt", "Тестовый", "Клиент", "user3@example.com", False),
]
for username, password, first, last, email, staff in USERS:
    user, created = User.objects.get_or_create(username=username, defaults=dict(
        first_name=first, last_name=last, email=email, is_staff=staff))
    if created:
        user.set_password(password)
        user.save()
group, _ = Group.objects.get_or_create(name="Пользователи сайта")  # без разрешений
User.objects.get(username="Пользователь_1").groups.add(group)
users = {u.username: u for u in User.objects.all()}

# --- компании (ЛР 6) ------------------------------------------------------
Company.objects.update_or_create(id=1, defaults=dict(
    name="ООО «Канцтовары»", adress="г. Архангельск, пр. Ломоносова, д. 1"))
Company.objects.update_or_create(id=2, defaults=dict(
    name="ООО «Бумажный мир»", adress="г. Архангельск, ул. Воскресенская, д. 5"))

# --- продукты (ЛР 4, 5, 6, 10, 16); id=2 в методичке был удалён ----------
Product.objects.update_or_create(id=1, defaults=dict(
    title="Карандаш простой HB", description="Чернографитный карандаш твёрдости HB",
    ves="25", company_id=1, slug="карандаш-простой-hb", image="images/karandash.png"))
Product.objects.update_or_create(id=3, defaults=dict(
    title="Тетрадь", description="Тетрадь в клетку, 48 листов",
    ves="", company_id=2, slug="тетрадь", image="images/tetrad.png"))
Product.objects.update_or_create(id=4, defaults=dict(
    title="Линейка", description="Линейка 30 см",
    ves="15", company_id=None, slug="линейка", image="images/lineyka.png"))

# --- статусы и экземпляры продуктов (ЛР 6, 13) ----------------------------
# id=2 «В заказе» используют страницы /borrowed/ и /all_borrowed/
for sid, name in [(1, "На складе"), (2, "В заказе"), (3, "Продана")]:
    Status.objects.update_or_create(id=sid, defaults={"name": name})

for iid, inv, product, status, due, customer in [
    (1, "1_1_1", 1, 1, None, None),
    (2, "1_1_2", 1, 2, date(2026, 10, 15), "Пользователь_2"),
    (3, "2_3_1", 3, 2, date(2026, 11, 20), "Пользователь_1"),
    (4, "2_3_2", 3, 1, None, None),
]:
    ProductInstance.objects.update_or_create(id=iid, defaults=dict(
        inv_number=inv, product_id=product, status_id=status, due_back=due,
        customer=users.get(customer)))

# --- прайс-лист и его позиции (ЛР 16, 17); корзина берёт цены отсюда ------
Price.objects.update_or_create(id=1, defaults={"number": 1})
Price.objects.filter(id=1).update(data=date(2026, 9, 30))  # auto_now_add
for pid, product, cost in [(1, 1, 25), (2, 3, 40), (3, 4, 30)]:
    Pozition_Price.objects.update_or_create(id=pid, defaults=dict(
        number_pricelist_id=1, product_price_id=product, cost_product=cost))

print("Готово: компаний", Company.objects.count(), "| продуктов", Product.objects.count(),
      "| экземпляров", ProductInstance.objects.count(), "| позиций прайса",
      Pozition_Price.objects.count(), "| пользователей", User.objects.count())
