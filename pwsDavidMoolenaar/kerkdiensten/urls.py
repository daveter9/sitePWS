from django.conf.urls import url
from . import views

app_name = 'kerkdiensten'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^voeg_kerk_toe', views.kerk_add, name='voeg_kerk_toe'),
    url(r'^dienst/(?P<dienst_id>[0-9]+)/$', views.dienst, name='dienst'),
    url(r'^rooster/$', views.rooster, name='rooster'),
    url(r'^rooster/maak_rooster/$', views.rooster_maak, name='maak_rooster'),
    url(r'rooster/zet_beschikbaarheid_vast', views.toggle_beschikbaarheid, name='toggle_beschikbaarheid'),
    url(r'^rooster/muzikanten/$', views.rooster_muzikanten, name='rooster_muzikanten')
]
