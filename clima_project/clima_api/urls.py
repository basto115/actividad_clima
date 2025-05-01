from django.urls import path
from .views import ClimaView

urlpatterns = [
    path('clima/', ClimaView.as_view()),
]