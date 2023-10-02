from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser
from tenant.models import Client


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15 ,unique=True)
    email = models.EmailField(max_length=255,unique=True)
    username = models.CharField(max_length=255,unique=True)  
    is_active = models.BooleanField(default=True)
    is_verified = models.IntegerField(choices=[(0, 'Not verified'), (1, 'Verified')], default=0)
    created_by = models.IntegerField(null=True)
    remarks = models.CharField(max_length=200,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    SUPERADMIN = 1
    ADMIN = 2
    PUBLISHER = 3
    ADVERTISER = 4
    USER = 5
    
    ROLE_CHOICES = (
        (SUPERADMIN, 'SUPERADMIN'),
        (ADMIN, 'ADMIN'),
        (PUBLISHER, 'PUBLISHER'),
        (ADVERTISER, 'ADVERTISER'),
        (USER, 'USER'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)
    tenant = models.ForeignKey(Client,related_name="users",on_delete=models.DO_NOTHING,default=None,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','tenant']

    def getRoleName(self):
        if self.role==1:
            return 'SUPERADMIN'
        else:
            return 'None'
    



