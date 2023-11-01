from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def drink_list(request, format=None):

    # get all the drinks
    # serialize them
    #return json

    if request.method == 'GET':
        drinks = Drink.objects.all()
        serializier = DrinkSerializers(drinks, many=True)
        return Response(serializier.data)

    if request.method == 'POST':
        serializier = DrinkSerializers(data=request.data)
        if serializier.is_valid():
            serializier.save()
            return Response(serializier.data, status=status.HTTP_201_CREATED)
@api_view(['GET', 'PUT', 'DELETE'])
def drink_detail(request, id, format=None):

    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
       serializers = DrinkSerializers(drink)
       return Response(serializers.data)
    elif request.method == 'PUT':
        serializers = DrinkSerializers(drink, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
