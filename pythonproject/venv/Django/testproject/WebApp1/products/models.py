from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse

# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=120,verbose_name=" Название компании")
    adress=models.CharField(max_length=120,verbose_name="Адрес компании")

    def __str__(self):
        return self.name

class Product(models.Model):
    title       = models.CharField(max_length=120,verbose_name="Название") # поле длиной в 120 символов
    description = models.TextField(blank=True, null=True,verbose_name="Описание")
    ves         =models.TextField(blank=True,verbose_name="Вес,г") # поле, в котором указывается вес продукта
    company=models.ForeignKey(Company,on_delete=models.CASCADE,blank=True, null=True,verbose_name='Компания поставщик')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name="для URL-продукта",allow_unicode=True)#url-продукта
    image = models.ImageField(upload_to='images/', blank=True,verbose_name="Изображение")

    class Meta:
        ordering = ['company']
        index_together = (('id', 'slug'),)#чтобы задать единый индекс для полей id и slug.
        #Данный индекс нужен для запроса продукта по ним.
        #
        # Оба поля индексируются вместе для улучшения представлений для запросов, использующих эти два поля.
    def __str__(self):
        return self.title
     #данный метод позволяет отобразить наименование конкретного продукта из БД на панели Алминистратора

    class Meta:
        verbose_name="Продукт",#метод позвляет видеть фразу "Продукт" ,
        #находясь в панели Администратора и изменяя информацию о выбранном продукте

        verbose_name_plural="Продукты"# метод позволяет отображать название модели Product как "Продукты",
        # когда не включена функция перевода

    def get_absolute_url(self):
        return reverse('detail_product',
                        args=[self.id])

class Status(models.Model):
    name=models.CharField(max_length=120,verbose_name="Статус продукта")
    def __str__(self):
        return self.name

class ProductInstance(models.Model):
    product=models.ForeignKey('Product',on_delete=models.CASCADE,blank=True, null=True)
    inv_number=models.CharField(max_length=120,verbose_name="Инвентарный номер")
    status=models.ForeignKey('Status',on_delete=models.CASCADE,blank=True, null=True,verbose_name="Статус продукта")
    due_back=models.DateField(blank=True, null=True,verbose_name="Дата  окончания статуса продукта")
    customer=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True, null=True,verbose_name="Заказчик")

    def __str__(self):
        return '%s %s %s' % (self.inv_number,self.product, self.status)
        # в таком содержании объект будет отображаться в admin панели

class Price (models.Model):
    number = models.IntegerField(verbose_name="Номер прайс-листа")
    data=models.DateField(verbose_name="Дата утверждения прайс-листа",auto_now_add=True)

    def __str__(self):
        #Строка для представления объекта Status в Admin Site
        return '№ %s от %s' % (self.number,self.data)
    #Метаданные
    class Meta:
        ordering = ['number']# сортировка по возрастанию

class Pozition_Price(models.Model):
    number_pricelist=models.ForeignKey('Price',on_delete=models.CASCADE,blank=True, null=True,verbose_name="Номер прайс-листа")
    product_price=models.ForeignKey('Product',on_delete=models.CASCADE,blank=True, null=True,verbose_name="Название продукта")
    cost_product=models.DecimalField(max_digits=7,decimal_places=2,blank=True, null=True,verbose_name="Цена продукта в прайс-листе")

    def __str__(self):
        #Строка для представления объекта Status в Admin Site
        return '%s %s' % (self.product_price,self.cost_product)
    #Метаданные
    class Meta:
        ordering = ['product_price']# сортировка по возрастанию
