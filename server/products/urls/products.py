from django.urls import path

from products.views import product_detail, product_list

app_name = 'products'

urlpatterns = [
    path('<int:pk>', product_detail, name='detail'),
    path('', product_list, name='main'),
]
