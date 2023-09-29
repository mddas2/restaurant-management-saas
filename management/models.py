from django.db import models


class FoodCategory(models.Model):
    """
    Model for different food categories.
    different types of roti are in roti items category.
    ex: 'roti items' contains butter roti, naan roti etc.
    """
    name = models.CharField(max_length=80)
    
    def __str__(self):
        return self.name


class MenuCategory(models.Model):
    """
    Model for associating food items with different menus like 
    Dining Menu ,Delivery Menu etc.
    """
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class FoodItem(models.Model):
    """
    Model for particular food items. 
    ex: chicken momo, butter roti.
    """
    name = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    food_category = models.ForeignKey(
        'FoodCategory', on_delete=models.SET_NULL, null=True
    )
    menu_category = models.ManyToManyField('MenuCategory')
    
    def __str__(self):
        return self.name