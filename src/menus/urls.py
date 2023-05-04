from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet

router = DefaultRouter()
router.register('', MenuViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
