
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from theme.views import change_theme
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("switch-theme/", change_theme, name="change-theme"),
    path("", include("we_site.urls")),
    path("__reload__/", include("django_browser_reload.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)