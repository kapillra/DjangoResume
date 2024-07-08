from django.urls import path
from .views import *

urlpatterns = [
    path('', login_page, name="login_page"),
    path('register_page/', register_page, name="register_page"),
    path('reset_password_page/', reset_password_page, name="reset_password_page"),
    path('profile_page/', profile_page, name="profile_page"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('profile_update/', profile_update, name="profile_update"),
    path('change_password/', change_password, name="change_password"),
]