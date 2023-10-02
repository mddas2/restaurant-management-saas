from django.db import models

# Create your models here.

class TableAndSpace(models.Model):
    """
    Model for mananging tables and spaces in the restaurant.
    """
    class Status(models.TextChoices):
        AVAILABLE = 'AV', 'Available'
        OCCUPIED = 'OC', 'Occupied'
        RESERVED = 'RE', 'Reserved'
    
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.AVAILABLE)
    capacity = models.IntegerField()
    location = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name