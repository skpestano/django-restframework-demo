from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializer import OrderSerializer, OrderItemSerializer
from .models import Orders, OrderItems

# Create your views here.
def orders(request):
    '''
    List all orders from the user
    '''
    if (request.method == 'GET'):
        orders = Orders.objects.all(id=request.user.id)
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if (request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = OrderSerializer(data=data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)
        

def order_items(request, order_id):
    '''
    List all items from the order 
    '''
    if (request.method == 'GET'):
        items = OrderItems.objects.all(order=order_id)
        serializer = OrderItemSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    if (request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = OrderItemSerializer(data=data)
        if (serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors, status=400)