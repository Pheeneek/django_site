from django.urls import path

from .views import ProductView, CartView, IndexView, ShopView


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('product/', ProductView.as_view()),
    path('cart/', CartView.as_view()),
    path('shop/', ShopView.as_view(), name='shop'),
    path('shop/<int:page>', ShopView.as_view()),
]
