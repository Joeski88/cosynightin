"""url path config """
from django.contrib import admin
from django.urls import path, include
from .views import handler404, handler500


urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),    
    path('summernote/', include('django_summernote.urls')),
    path("", include("cniapp.urls"), name='cniapp-urls'),
]

handler404 = 'cniproject.views.handler404'
handler500 = 'cniproject.views.handler500'