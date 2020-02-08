from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from fitclip.common.paginations import SmallResultsSetPagination
from fitclip.mall.models.product import Product
from fitclip.mall.serializers.product import ProductSerializer, ProductDetailSerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = SmallResultsSetPagination

    @action(detail=True, url_path='detail')
    def product_detail(self, request, pk=None):
        product: Product = self.get_object()
        serializer = ProductDetailSerializer(product.detail)

        return Response(serializer.data)

