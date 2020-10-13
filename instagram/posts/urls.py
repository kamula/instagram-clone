from django.urls import path
from .views import homescreen_view
urlpatterns = [
    path("post",homescreen_view,name = "home")
]
