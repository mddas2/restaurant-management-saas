from django.db import models
from management.models import FoodItem
from tableandspace.models import Table

# Create your models here

class Order(models.Model):
    """Model for Order """
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    )

    # Basic order information
    order_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    item_name=models.CharField(max_legth=20)

    abstract=True
    def __str__(self):
        return f"Order #{self.order_number}"

    class Meta:
        ordering = ['-created_at']

class InHouseOrder(Order):
    """ Model for Order in side the Restraunant"""
    #Table Information
    table_number=models.ManyToManyField(Table,related_name='inhouseorder')
    #Food Item Information
    food_items=models.ManyToManyField(FoodItem,)

class DeliveryOrder(Order):
    """ Model For Delivery """
    food_items= models.ManyToManyField(FoodItem,)
    delivery_address=models.CharField(max_length=50)


class IndividualTableBill(models.Model):


