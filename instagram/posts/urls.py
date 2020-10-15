from django.urls import path
from .views import homescreen_view,create_post_view
urlpatterns = [
    path("post",homescreen_view,name = "home"),
    path('create',create_post_view, name="createPost")
]
