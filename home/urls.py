from django.urls import path
from . import views
urlpatterns = [
    path("", views.index),
    path("about/",views.about),
    path("login/",views.login, name="loginpage"),
    path("afterlogin/",views.afterlogin, name="afterlogin"),
    path("register/",views.register),
    path("services/",views.services),
    path("contact/",views.contact),
    path("blog/",views.blog),
    path("logout/",views.logout),
    path("myblog/",views.myblog),
]