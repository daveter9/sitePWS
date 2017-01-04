from django.contrib import admin
from .models import Kerken, User_details, Rollen, Kerkdiensten, DienstSoorten, UserRoll, Instrumenten, MuziekTeams


class KerkdienstenAdmin(admin.ModelAdmin):
    model = Kerkdiensten
    filter_horizontal = ('beschikbaar','ingeroosterd')

class User_detailsAdmin(admin.ModelAdmin):
    model = User_details
    filter_horizontal = ('rollen_v2',)

class MuziekTeamAdmin(admin.ModelAdmin):
    model = MuziekTeams
    filter_horizontal = ('leden',)

admin.site.register(Kerken)
admin.site.register(Rollen)
admin.site.register(DienstSoorten)
admin.site.register(User_details, User_detailsAdmin)
admin.site.register(Kerkdiensten, KerkdienstenAdmin)
admin.site.register(UserRoll)
admin.site.register(Instrumenten)
admin.site.register(MuziekTeams, MuziekTeamAdmin)
