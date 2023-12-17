from django.urls import path
from .views import (
        stock_list,
        stock_create,
        stock_detail,
        stock_update,
        stock_delete,
        stock_receive,
        stock_issue,
        )

urlpatterns = [
        path('', stock_list, name = 'stock_list'),
        path('stock_create/', stock_create, name = 'stock_create'),
        path('stock_detail/<int:pk>/', stock_detail, name = 'stock_detail'),
        path('stock_update/<int:pk>/', stock_update, name = 'stock_update'),
        path('stock_delete/<int:pk>/', stock_delete, name = 'stock_delete'),
        path('stock_receive/<int:pk>/', stock_receive, name = 'stock_receive'),
        path('stock_issue/<int:pk>/', stock_issue, name = 'stock_issue'),
        ]
