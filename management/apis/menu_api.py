from rest_framework import viewsets

from management.models import FoodItem, FoodCategory, MenuCategory
from management.serializers import menu_serializers


class FoodItemViewSet(viewsets.ModelViewSet):
    queryset = FoodItem.objects.all()
    serializer_class = menu_serializers.FoodItemSerializer
    
    
class FoodCategoryViewSet(viewsets.ModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = menu_serializers.FoodCategorySerializer
    
    
class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = menu_serializers.MenuCategorySerializer