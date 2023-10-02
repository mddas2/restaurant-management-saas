from django.urls import path, include
from .views import TableAndSpaceViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tableandspace', TableAndSpaceViewSet, basename='tableandspace')    

urlpatterns = [
    path('', include(router.urls)),
]