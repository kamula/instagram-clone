from django.urls import path
from .views import homescreen_view
urlpatterns = [
    path("register",homescreen_view,name = "home")
]
