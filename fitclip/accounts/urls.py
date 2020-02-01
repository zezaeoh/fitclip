from django.urls import path
from .views import UserProfileListCreateView, UserProfileDetailView

urlpatterns = [
    path("profiles/<int:pk>", UserProfileDetailView.as_view(), name="profile"),
    path("profiles/", UserProfileListCreateView.as_view(), name="profiles"),
]
