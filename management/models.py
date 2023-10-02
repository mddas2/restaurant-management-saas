from django.db import models
from tenant.models import ResturentAwareModel


class FoodCategory(ResturentAwareModel):
    """
    Model for different food categories.
    different types of roti are in roti items category.
    ex: 'roti items' contains butter roti, naan roti etc.
    """
    name = models.CharField(max_length=80)
    food_item = models.ManyToManyField('FoodItem', blank=True, related_name='food_category')
    
    def __str__(self):
        return self.name


class MenuCategory(ResturentAwareModel):
    """
    Model for associating food items with different menus like 
    Dining Menu ,Delivery Menu, Special Menu etc.
    """
    name = models.CharField(max_length=100)
    food_item = models.ManyToManyField('FoodItem', blank=True, related_name='menu_category')
    
    def __str__(self):
        return self.name


class FoodItem(ResturentAwareModel):
    """
    Model for particular food items. 
    ex: chicken momo, veg momo, butter roti.
    """
    name = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    
    def __str__(self):
        return self.name