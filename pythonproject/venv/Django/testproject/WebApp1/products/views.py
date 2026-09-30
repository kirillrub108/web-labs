from django.shortcuts import render, redirect

# Подключение стандартной формы для регистрации
from django.contrib.auth.forms import UserCreationForm

from products.forms import RegistrForm

from django.http import HttpResponseRedirect

from .forms import ProductForm

from .models import Product, Company, ProductInstance, Pozition_Price #импортируем из моделей приложения products модель Product
# чтобы иметь возможность работать с данными этой модели (таблицы БД)

from django.urls import reverse

# Create your views here.
def product_detail_view(request):
    obj=Product.objects.all()#метод all() позволяет получить информацию
                             #о всех объектах (записях таблицы) модели Product
    context={
        "my_obj":obj,
    }
    return render(request, "product/detail.html",context)

def product_detail_1_view(request,id):
    obj_1=Product.objects.get(id=id) #метод get() позволяет получить информацию
                                     #об идентификаторе (id продукта) модели Product  в данном случае
    context={
        "my_obj_1":obj_1,
    }
    return render(request, "product/detail_product.html",context)

def product_create_view(request):
    form=ProductForm()
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid(): # проверка на валидность формы, т.е. на правильность введенных всех данных
            Product.objects.create(**form.cleaned_data)
            # символы ** использованы т.к. фтрибуты формы совпадант с полями модели Product
    form=ProductForm() # очистка содержимого формы
    context={
        "form":form,
    }
    return render(request, "product/product_create.html",context)

def product_delete_view(request,id):
    obj_2=Product.objects.get(id=id) #метод get() позволяет получить информацию
                                     #об идентификаторе (id продукта) модели Product  в данном случае
    obj_2.delete()

    return redirect(reverse('product_detail')) # метод возвращает на страницу, на кот.  указана в скобках функции reverse()

def product_edit_view(request,id):
    get_product=Product.objects.get(id=id)
    if request.method=='POST':
            get_product.title=request.POST.get('title')
            get_product.description=request.POST.get('description')
            get_product.ves=request.POST.get('ves')
            get_product.save()
            return HttpResponseRedirect("/detail")

    else:
        return render(request,"product/edit_product.html",{'get_product':get_product} )

def index_view(request):
    num_product=Product.objects.all().count()# общее количество продуктов
    num_company=Company.objects.all().count() # общее количество компаний
    num_instance=ProductInstance.objects.all().count()
    num_instance_available=ProductInstance.objects.filter(status_id__exact=2).count()
    # вычисление количества продуктов, доступных к заказу, т.е. имеющих статус "На складе"
    context={
        'num_product':num_product,
        'num_company':num_company,
        'num_instance':num_instance,
        'num_instance_available':num_instance_available,
    }
    return render(request,"home.html",context )

from django.views import generic

class CompanyView(generic.ListView):
    model=Company

from django.contrib.auth.mixins import LoginRequiredMixin

class LoanedProductByUserListView(LoginRequiredMixin,generic.ListView) :
    model =ProductInstance
    template_name='product/productinstance_list_customer_user.html'
    paginate_by=10

    def get_queryset(self) :
        return ProductInstance.objects.filter(customer=self.request.user).filter(status_id__exact=2).order_by('due_back')


class LoanedProductAllListView(generic.ListView):
    model = ProductInstance
    template_name='product/productinstance_list_borrowed_all.html'
    context_object_name ='productinstance_list'


    def get_queryset(self):
        return ProductInstance.objects.filter(status_id__exact=2).order_by('-due_back')


def registrat(request):
    # Массив для передачи данных шаблонна
    #Содержимое массива будет передаваться в качестве контекста
    data = {}
    # Проверка что есть запрос POST

    if request.method == 'POST':
        # Создание формы
        form = RegistrForm(request.POST)
        # Валидация данных из формы
        if form.is_valid():
            # Сохранение пользователя
            new_user=form.save(commit=False)
            #new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            # Передача формы к рендару
            data['form'] = form
            # Рендаринг страницы
            return render(request, 'registration/registration_out.html', data)
    else:
        # Создание формы
        form = RegistrForm()
        # Передача формы для рендеринга
        data['form'] = form
        # Рендаринг страницы
    return render(request, 'registration/registration.html', data)

def product_list(request):

    #products =Product.objects.filter(productinstance__status_id__exact=1)
    products=Pozition_Price.objects.all()
    context={
        'products': products,
        }
    return render(request,'products/product_list.html',context)



from cart.forms import CartAddProductForm

def product_detail(request, id):
    #product = Product.objects.get(id=id,slug=slug)
    product=Pozition_Price.objects.get(product_price_id=id)
    cart_product_form = CartAddProductForm()
    return render(request, 'products/product_detail.html', {'product': product,
                                                            'cart_product_form': cart_product_form})
