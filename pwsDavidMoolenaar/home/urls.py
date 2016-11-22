from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views
from .forms import LoginForm

app_name = 'home'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, {'template_name': 'home/login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', auth_views.logout, {'next_page':'/'}, name='logout'),
]
