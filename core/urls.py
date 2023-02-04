from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register("parts", PartViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path("get-parts", PartView.as_view(), name="path"),
    path('import-csv/', import_csv, name='import_csv'),
]