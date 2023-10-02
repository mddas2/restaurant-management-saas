from django.db import models
from management.models import FoodItem
# from tableandspace.models import Table
from account.models import CustomUser


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
    guest_number = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    item_id = models.ForeignKey(FoodItem,related_name="order")
    item_name=models.CharField(max_legth=20)
    item_price=models.CharField(max_legth=20)
    item_description=models.CharField(max_legth=20)

    order_type = models.CharField(max_legth=20)
    table = models.CharField(max_legth=20)

    def __str__(self):
        return f"Order #{self.order_number}"

    class Meta:
        ordering = ['-created_at']

class InHouseOrder(models.Model):
    """ Model for Order in side the Restraunant"""

    orders=models.ManyToManyField(Order,related_name='inhouseorder')
    table = models.CharField(max_legth=20)
    total_price = models.CharField(max_legth=20)
    status =  models.CharField(max_legth=20)
   

class DeliveryOrder(models.Model):
    """ Model For Delivery """
    
    orders=models.ManyToManyField(Order,related_name='inhouseorder')
    user=models.ForeignKey(CustomUser,related_name="order_delivery")
    status =  models.CharField(max_legth=20)


# class IndividualTableBill(models.Model):



