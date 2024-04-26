"""URL configuration for coffee_guide project."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
# from users.views import auth

app_name = 'social'


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
         "swagger/",
         SpectacularSwaggerView.as_view(url_name="schema"),
         name="swagger",
     ),
     path(
         "redoc/",
         SpectacularRedocView.as_view(url_name="schema"),
         name="redoc",
     ),
    re_path('', include('social_django.urls', namespace='social')),
    #path("auth/", auth),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
