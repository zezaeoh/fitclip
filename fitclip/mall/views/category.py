from rest_framework import viewsets, permissions

from fitclip.common.paginations import SmallResultsSetPagination
from fitclip.mall.models.category import Category, Section, Sub
from fitclip.mall.serializers.category import CategorySerializer, SectionSerializer, SubSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = SmallResultsSetPagination


class SectionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing sections.
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = SmallResultsSetPagination


class SubViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing subs.
    """
    queryset = Sub.objects.all()
    serializer_class = SubSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = SmallResultsSetPagination

