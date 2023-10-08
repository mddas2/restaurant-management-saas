from rest_framework import serializers
from .models import Restaurant, RestaurantTenantAwareModel

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
    
class  RestaurantAwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantTenantAwareModel
        fields = '__all__'