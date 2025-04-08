from rest_framework import serializers
from .models import Country,Item

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__' 