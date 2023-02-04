from rest_framework import serializers
from .models import *



class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"


class PartSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(many=True)

    class Meta:
        model = Part
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

class SubCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'category')