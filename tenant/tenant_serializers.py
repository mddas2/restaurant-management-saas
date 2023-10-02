from rest_framework import serializers
from .models import Resturent,ResturentTenantAwareModel

class ResturentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resturent
        fields = '__all__'
    
class  ResturentAwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResturentTenantAwareModel
        fields = '__all__'