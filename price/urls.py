from rest_framework.routers import DefaultRouter

from price.api import views

router = DefaultRouter()
router.register(r"price", views.PriceViewSet, basename="price")

urlpatterns = router.urls
