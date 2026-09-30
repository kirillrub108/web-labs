"""
URL configuration for WebApp1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views # ИНСТРУКЦИЯ ПО ИМПОРТУ ПРЕДСТАВЛЕНИЯ
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include

from django.conf.urls.static import static
from django.conf import settings

from pages import views
from products.views import product_detail_view

from products.views import product_detail_1_view, product_create_view
from products.views import product_delete_view
from products.views import product_edit_view
from products.views import index_view

from django.urls import re_path

from products.views import CompanyView

from django.urls import include

from products.views import LoanedProductByUserListView, LoanedProductAllListView

from products.views import registrat

from products.views import product_list

urlpatterns = [
    path('admin/', admin.site.urls),# путь, для попадания в панель администратора

    path('',include('products.urls')),

    path('',include('cart.urls')),

    #path('', views.home_view, name='home'),# путь, для попадания в нашу страницу home.html

    path('', index_view, name='home'),# путь, для попадания в нашу страницу home.html

    path('contact/', views.contact_view),# путь, для попадания в нашу страницу contact_view

    path('about/', views.about_view),# путь, для попадания в нашу страницу about_view

    path('social/', views.social_view),# путь, для попадания в нашу страницу social_view

    path('detail/', product_detail_view, name='product_detail'),

    path('detail_product/<int:id>', product_detail_1_view),

    path('create/', product_create_view),

    path('product_delete/<int:id>', product_delete_view, name='delete_product'),

    path('product_edit/<int:id>', product_edit_view, name='edit_product'),

    re_path('company_list/',CompanyView.as_view(),name='company'),

    re_path('product_list/',product_list,name='product_list'),

    path('accounts/',include('django.contrib.auth.urls')),

    re_path('all_borrowed/', LoanedProductAllListView.as_view(), name='all-borrowed'),

    re_path('borrowed/',LoanedProductByUserListView.as_view(),name='my-borrowed'),

    path('registr/',registrat),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
