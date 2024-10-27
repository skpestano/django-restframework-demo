from rest_framework import serializers
from .models import Orders, OrderItems

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orders
        fields = ['id', 'user', 'user_name', 'status', 'total_amount', 'shipping_address', 'phone_number','created_at']

class OrderItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OrderItems
        fields = ['id', 'order','product','name','quantity']