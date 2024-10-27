from django.urls import path 
from . import views

urlpatterns = [
    path('api/', views.products),
    path('api/<int:product_id>', views.product_item)
]