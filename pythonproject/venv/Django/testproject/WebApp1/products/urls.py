
from django.urls import path



from .views import product_list,product_detail


urlpatterns = [
    path('product_list/',product_list,name='product_list'),
    path('detail_product/<int:id>/',product_detail,name='detail_product'),

]
