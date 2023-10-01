from django.urls import path, include

from rest_framework.routers import DefaultRouter

from management.apis import menu_api


router = DefaultRouter()
router.register(r'food-item', menu_api.FoodItemViewSet)
router.register(r'food-category', menu_api.FoodCategoryViewSet)
router.register(r'menu', menu_api.MenuCategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
