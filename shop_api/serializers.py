from rest_framework import serializers

from shop.models import User, Product, Coupone, Cart


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"

        fields = [
            'first_name',
            'last_name',
            'email'
        ]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CouponeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupone
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = (
            'id',
            'user',
            'product',
            'count'
        )










# from .models import User
# from shop.models import Cart, Product
#
#
#
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'
#
#
# class CartSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         fields = '__all__'
#
#
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Product
#         fields = '__all__'
