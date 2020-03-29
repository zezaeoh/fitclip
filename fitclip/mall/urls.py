from django.urls import path, include
from rest_framework.routers import DefaultRouter

from fitclip.mall.views.product import ProductViewSet
from fitclip.mall.views.category import CategoryViewSet, SectionViewSet, SubViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'sections', SectionViewSet)
router.register(r'subs', SubViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
