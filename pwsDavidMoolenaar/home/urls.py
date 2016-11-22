from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'),
   # url(r'^login/$', views.user_login, name='user_login'),
   url(r'^login/$', auth_views.login, {'template_name':'home/login.html'}),
    url(r'^register/$', views.user_register, name='user_register'),
]
