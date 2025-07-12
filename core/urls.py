from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.i18n import i18n_patterns, set_language
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Expense Tracker API",
      default_version='v1',
      description="Kirim Chiqim hisobotlarini olib borish dasturlari uchun API",
      contact=openapi.Contact(email="zepdeveloper404@gmail.com"),
      license=openapi.License(name="Codial License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('api/auth/', include('users.urls')),
    path('api/', include('main.urls')),

    #docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
urlpatterns += i18n_patterns(
    path('i18n/set-lang/', set_language, name='set_language'),
    path('admin/', admin.site.urls),
)

