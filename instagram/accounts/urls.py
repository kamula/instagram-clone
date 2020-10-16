from django.urls import path
from .views import registration_view,login_view, logout_view,account_view,must_authenticate_view
urlpatterns = [
    path('login',login_view,name='login'),
    path('register',registration_view,name='register'),
    path('logout',logout_view,name="logout"),   
    path('account',account_view,name="account"),   
    path('must_authenticate',must_authenticate_view,name="must_authenticate")   
]
