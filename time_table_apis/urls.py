from django.urls import re_path
from .views import register_user_view,login_user_view


urlpatterns=[
    re_path(r"^timetableapi/register-user/?$",register_user_view,name="register_user"),
    re_path(r"^timetableapi/login-user/?$",login_user_view,name="login_user")
]