from django.urls import path, include
from .views import home, login_view, dashboard, logout_view
urlpatterns = [
    # path("", index, name="index"),
    path("login/", login_view, name="login"),
    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path('logout/', logout_view, name='logout'),
    # path("login/", login_view, name="login"),

    
]
