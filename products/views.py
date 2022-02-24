from ast import Break
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import products


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
    return Response(products)

@api_view(['GET'])
def get_product(request , pk):
    print(pk)
    product = 'There is No product with the Given parameter !!!'
    for i in products:
        if i['_id'] == str(pk):
            product = i
            break;
    return Response(product)
