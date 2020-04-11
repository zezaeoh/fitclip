from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.request import Request
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin
from rest_framework.response import Response

from fitclip.common.paginations import SmallResultsSetPagination
from fitclip.fit.models.fit_store import FitStore
from fitclip.fit.serializers import FitStoreSerializer


class FitStoreViewSet(
    RetrieveModelMixin,
    CreateModelMixin,
    viewsets.GenericViewSet
):
    queryset = FitStore.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FitStoreSerializer
    pagination_class = SmallResultsSetPagination

    def get_object(self):
        queryset = self.get_queryset()
        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {
            'sub_id': self.kwargs['sub_id'],
            self.lookup_field: self.kwargs[lookup_url_kwarg]
        }
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

    def list(self, request: Request, sub_id: int = None):
        queryset = self.get_queryset().filter(user_id=request.user.id, sub_id=sub_id)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request: Request, sub_id: int = None, **kwargs):
        serializer = self.get_serializer(data={
            **request.data,
            'sub': sub_id,
            'user': request.user.id
        })
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
