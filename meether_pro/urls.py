from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


# this modules were imported to handle file and picture upload
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('api/', include('api.urls')),
    path('meether_app/', include('meether_app.urls')),
    path('auth/', obtain_auth_token)
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)