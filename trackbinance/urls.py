from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

import price.urls
from trackbinance import settings


class ExtendableRouter(routers.DefaultRouter):
    def extend(self, router):
        self.registry.extend(router.registry)


router = ExtendableRouter()
router.extend(price.urls.router)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("ht/", include("health_check.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
