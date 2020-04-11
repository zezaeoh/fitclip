from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FitStoreViewSet

router = DefaultRouter()
router.register(r'(?P<sub_id>\d+)/stores', FitStoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
