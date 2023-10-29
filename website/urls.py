from django.urls import path
from .views import indexview


urlpatterns = [
    path("", indexview.as_view())
]
