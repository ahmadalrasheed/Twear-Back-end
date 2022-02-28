from ast import Break
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product


# Create your views here.
@api_view(["GET"])
def get_routes(request):
    routes = [
        "test/test",
        "test/test",
        "test/test",
        "test/test",
        "test/test",
        "test/test",
    ]
    return Response(routes)


@api_view(["GET"])
def get_products(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_product(request, pk):
    product = "There is No product with the Given parameter !!!"
    all_product = Product.objects.all()
    serializer = ProductSerializer(all_product, many=True)
    for i in serializer.data:
        if i["_id"] == pk:
            product = i
            break
    return Response(product)
