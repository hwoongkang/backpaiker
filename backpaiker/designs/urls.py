from rest_framework import routers
from .api import DesignViewSet

router = routers.DefaultRouter()
router.register("api/designs", DesignViewSet, "designs")

urlpatterns = router.urls

