# from django.shortcuts import render
from rest_framework import viewsets
from .models import Country,Item
from .serializers import CountrySerializer,ItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
# Create your views here.

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class ItemsView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
class ItemPartialUpdateView(APIView):
     
    def patch(self, request, item_id): 
        try:
            #Retrieve the item by Id 
            item = Item.objects.get(id=item_id) 
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        #Partially update with incoming data serializer Itemserializer(item, data-request.data, partial-True)
        serializer = ItemSerializer(item, data=request.data, partial=True) # set partial=True to update a data partially
        if serializer.is_valid():

        #Save only the fields provided 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    