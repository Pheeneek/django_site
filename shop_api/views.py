from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.decorators import action
from  rest_framework import status

from django.db.models import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


from shop.models import User, Product, Coupone, Cart
from .serializers import UserSerializer, ProductSerializer, CouponeSerializer, CartSerializer

# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()  # новая копия данных из БД

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        filter_kwargs = {param: request.GET[param] for param in request.GET}

        filter_queryset = queryset.filter(**filter_kwargs)
        serializer = self.get_serializer(filter_queryset, many=True)

        return Response(serializer.data)


class CouponeViewSet(GenericViewSet):

    queryset = Coupone.objects.all()
    serializer_class = CouponeSerializer

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(obj)

        return Response(serializer.data)


class CartViewSet(ListModelMixin,
                  CreateModelMixin,
                  RetrieveModelMixin,
                  DestroyModelMixin,
                  GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = 'product__type'

    @action(detail=True, methods=['get'])
    def delete(self, request, pk=None):
        """
        /carts/1/delete  # detail=True

        :param request:
        :param pk:
        :return:
        """
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    # def list(self, request):
    #     if 'type' in request.GET:
    #         filter_queryset = self.get_queryset().filter(product__type=request.GET['type'])
    #         serializer = self.get_serializer(filter_queryset, many=True)
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     else:
    #         return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)





























#
# class CartViewSet(ModelViewSet):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer
#
#     def list(self, request, *args, **kwargs):
#         return super().list(request, request, *args, **kwargs)
#
#
# class ProductViewSet(ReadOnlyModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#
#     def list(self, request, *args, **kwargs):
#         filter_queryset = self.queryset
#         if 'type' in request.GET:
#             filter_queryset = self.queryset.filter(type=request.GET['type'])
#
#         serializer = self.get_serializer(filter_queryset, many=True)
#         return Response(serializer.data)
