
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "ANAND ICE CREAM ADMIN"
admin.site.site_title = "ANAND ICE CREAM Admin Portal"
admin.site.index_title = "Welcome to ANAND ICE CREAMS"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
]
