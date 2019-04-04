from django.urls import path

from products.views import (
    product_detail, product_list, product_create,
    product_update, product_delete, product_rest_list,
    ProductCreate, ProductUpdate, ProductDelete
)

app_name = 'products'

urlpatterns = [
    path('create/', ProductCreate.as_view(), name='create'),
    path('<int:pk/update>', ProductUpdate.as_view(), name='update'),
    path('<int:pk/delete>', ProductDelete.as_view(), name='delete'),
    path('<int:pk>', product_detail, name='detail'),
    path('', product_list, name='main'),
]
urlpatterns += [
    path('api/', product_rest_list, name='rest_list')

]