from django.contrib import admin
from .models import Kerken, User_details, Rollen, Kerkdiensten, DienstSoorten

admin.site.register(Kerken)
admin.site.register(User_details)
admin.site.register(Rollen)
admin.site.register(Kerkdiensten)
admin.site.register(DienstSoorten)