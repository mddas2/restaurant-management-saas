from django.contrib import admin

from .models import InHouseOrder, DeliveryOrder, IndividualTableBill
# Register your models here.
admin.site.register([InHouseOrder, DeliveryOrder, IndividualTableBill])