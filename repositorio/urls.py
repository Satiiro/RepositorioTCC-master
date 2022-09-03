from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('', include('tcc.urls')),
    path('', include('usuario.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)