from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('commander/', views.order_create, name='order_create'),
    path('mes-commandes/', views.order_list, name='order_list'),
    path('commande/<int:order_id>/', views.order_detail, name='order_detail'),
]
