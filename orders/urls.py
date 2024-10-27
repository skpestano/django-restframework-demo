from django.urls import path 
from . import views

urlpatterns = [
    path('api/', views.orders),
    path('api/<int:order_id>', views.order_items)
]