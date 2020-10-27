from rest_framework import routers

from .views import UserViewSet, ProductViewSet, CouponeViewSet, CartViewSet

router = routers.SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)
router.register(r'coupones', CouponeViewSet)
router.register(r'carts', CartViewSet)

urlpatterns = router.urls

