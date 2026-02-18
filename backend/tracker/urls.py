from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, ApplicationViewSet

router = DefaultRouter()
router.register(r"companies", CompanyViewSet, basename="companies")
router.register(r"applications", ApplicationViewSet, basename="applications")

urlpatterns = router.urls
