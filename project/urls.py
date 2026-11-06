from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views import TeamViewSet, DriverViewSet

router = DefaultRouter()
router.register(r'teams', TeamViewSet)
router.register(r'drivers', DriverViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include(router.urls)), 
]
