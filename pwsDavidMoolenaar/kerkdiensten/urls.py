from django.conf.urls import url
from . import views

app_name = 'kerkdiensten'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^voeg_kerk_toe', views.kerk_add, name='voeg_kerk_toe'),
    url(r'^dienst/(?P<dienst_id>[0-9]+)/$', views.dienst, name='dienst'),
    url(r'^rooster/$', views.rooster, name='rooster')
]
