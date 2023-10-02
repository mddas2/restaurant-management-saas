from rest_framework import serializers
from  .models import TableAndSpace

class TableAndSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableAndSpace
        fields = '__all__'