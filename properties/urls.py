from rest_framework.routers import DefaultRouter

from properties.views import PropertiesView

router = DefaultRouter()

router.register('properties', PropertiesView.as_view(), basename='properties')

urlpatterns = router.urls
