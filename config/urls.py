from django.contrib import admin
from django.urls import path, include

from app1.views import CityDocumentView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
books = router.register("city", CityDocumentView, basename="citydocument")

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
]
