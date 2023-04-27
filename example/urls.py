from django.urls import path

from app.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
