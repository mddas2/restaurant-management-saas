from django.db import models


class MenuCategory(models.Model):
    name = models.CharField(max_length=150)
    
    
class FoodItem(models.Model):
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    
class FoodCategory(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    menu_category = models.ForeignKey('MenuCategory')
    
    
class MenuHaveFood(models.Model):
    menu_category = models.ForeignKey('MenuCategory')
