from django.contrib import admin

# Register your models here.
from .models import Company, Product, ProductInstance, Status, Price,Pozition_Price

admin.site.register(Price)
admin.site.register(Pozition_Price)

#admin.site.register(Product)//
class ProductInstanceInline(admin.TabularInline):
    model=ProductInstance

class ProductAdmin(admin.ModelAdmin):
    list_display=('title','description','ves','company','show_count') # Поля модели Product в том же порядке следования
    list_filter=('company',) #Возможность осуществлять фильтрацию данных
    prepopulated_fields = {'slug': ('title',)}# начение автоматически задается с использованием значения других полей
    #данное поле slug будет автоматически заполняться значением поля title
    inlines=[ProductInstanceInline] # добавление связной таблицы ProductInstance
    search_fields = ("title__startswith", ) # возможность поиска объектов по полю title
    def show_count(self, obj):#функция, вычисляющая количество связных объектов в таблице ProductInstance
        from django.db.models import Count
        result = ProductInstance.objects.filter(product=obj).aggregate(Count('product'))
        #Параметр obj — это объект для отображаемой строки.
        return result["product__count"]
    show_count.short_description = "Количество,шт"
admin.site.register(Product,ProductAdmin)
admin.site.register(Company)
admin.site.register(Status)
#admin.site.register(ProductInstance)
class ProductInstanceAdmin(admin.ModelAdmin):
    list_display=('inv_number','product','status')#Поля, отображаемые в административной панели
    list_filter=('product','status')
    fieldsets=(
        ('Экземпляр продукта',{
            'fields':('inv_number','product')
        }
        ),
        ('Статус и окончание его действия',{

                'fields':('customer','status','due_back')
            }
        )
    )
admin.site.register(ProductInstance,ProductInstanceAdmin)
