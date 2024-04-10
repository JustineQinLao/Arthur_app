from django.urls import path, include
from .views import index, home
urlpatterns = [
    # path("", index, name="index"),
    path("", home, name="home"),
]
