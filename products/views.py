from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import permissions, viewsets
from .models import Products
from .serializer import ProductSerializer
# Create your views here.
class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]


def products(request):

    if (request.method == 'GET'):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def product_item(request,product_id):
    if (request.method == "GET"):
        item = Products.objects.get(id=product_id)
        serializer = ProductSerializer(item)
        return JsonResponse(serializer.data)