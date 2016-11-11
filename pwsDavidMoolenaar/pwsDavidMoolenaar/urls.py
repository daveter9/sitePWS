from django.conf.urls import include, url
from django.contrib import admin
from pwsDavidMoolenaar.views import home

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('home.urls')),
    url(r'^$', home),
]
