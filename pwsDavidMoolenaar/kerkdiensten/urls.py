from django.conf.urls import url
from . import views

app_name = 'kerkdiensten'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^voeg_kerk_toe', views.kerk_add, name='voeg_kerk_toe')
]
