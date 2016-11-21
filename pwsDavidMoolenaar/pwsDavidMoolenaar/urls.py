from django.conf.urls import include, url
from django.contrib import admin
from pwsDavidMoolenaar.views import home, kerkdiensten

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls')),
    url(r'^kerkdiensten/', include('kerkdiensten.urls'))
]
