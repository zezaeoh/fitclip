from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fitclip.mall.views.product import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]