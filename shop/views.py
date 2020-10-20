from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, reverse
from django.core.paginator import Paginator, EmptyPage

from .models import Product, Cart
from .conf_info import info

# Create your views here.


class ProductView(View):

    def get(self, request):
        product = Product.objects.all()
        if 'type' in request.GET:
            product = product.filter(type=request.GET['type'])
        print(product)
        return HttpResponse(product)

    def post(self, request):
        params = request.POST
        product = Product(name=params['name'])
        try:
            product.save()
        except Exception as e:
            return HttpResponse(f"Product create error !")

        return HttpResponse(f"Product {list(params.items())} create successful!")


class CartView(View):
    def get(self, request):
        email = request.GET['email']
        cart = Cart.objects.filter(user__email=email).order_by('-create_at')

        return HttpResponse(cart)


class IndexView(View):

    def get(self, request):
        return render(request, 'shop/index.html', info)


class ShopView(View):

    def get(self, request, page=1):
        products_list = [
            {
                'name': 'Bell Pepper',
                'image': 'shop/images/product-1.jpg',
                'price': '$120.00',
                'discount': '30%',
                'price_sale': '$80.00'
            },
            {
                'name': 'Strawberry',
                'image': 'shop/images/product-2.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Green Beans',
                'image': 'shop/images/product-3.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Purple Cabbage',
                'image': 'shop/images/product-4.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Tomatoe',
                'image': 'shop/images/product-5.jpg',
                'price': '$120.00',
                'discount': '30%',
                'price_sale': '$80.00'
            },
            {
                'name': 'Brocolli',
                'image': 'shop/images/product-6.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Carrots',
                'image': 'shop/images/product-7.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Fruit Juice',
                'image': 'shop/images/product-8.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Onion',
                'image': 'shop/images/product-9.jpg',
                'price': '$120.00',
                'discount': '30%',
                'price_sale': '$80.00'
            },
            {
                'name': 'Apple',
                'image': 'shop/images/product-10.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Garlic',
                'image': 'shop/images/product-11.jpg',
                'price': '$120.00'
            },
            {
                'name': 'Chilli',
                'image': 'shop/images/product-12.jpg',
                'price': '$120.00'
            }
        ]
        prod_on_page = 3
        paginator = Paginator(products_list, prod_on_page)

        try:
            products_list = paginator.page(page)
            products_list.tuple_pages = tuple(paginator.page_range)
        except EmptyPage:
            redirect(reverse('shop'))

        context = {'product_list': products_list}
        context.update(info)

        return render(request, 'shop/shop.html', context)
