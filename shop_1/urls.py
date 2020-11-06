from django.urls import path

from .views import IndexView, ShopView

urlpatterns = [
    path('', IndexView.as_view()),
    path('shop_1/', ShopView.as_view(), name='shop'),
    path('shop_1/<int:page>', ShopView.as_view())
]
