from django.urls import path

from .views import ProductView, CartView, IndexView, ShopView


urlpatterns = [
    path('', IndexView.as_view()),
    path('product/', ProductView.as_view()),
    path('cart/', CartView.as_view()),
    path('shop/', ShopView.as_view()),
]
