from django.contrib.auth.models import User
from django.db import models


class User_details(models.Model):
    user = models.ForeignKey(User, default=1)
    kerk = models.ForeignKey('Kerken', default=None, blank=True, null=True)
    rollen_v2 = models.ManyToManyField('Rollen', blank=True, related_name='user_details_rollen_v2')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'user_details'

class Kerken(models.Model):
    kerk_naam = models.CharField(max_length=256)
    kerk_soort = models.CharField(max_length=256)

    def __str__(self):
        return self.kerk_naam

    class Meta:
        verbose_name_plural = 'kerken'

class Rollen(models.Model):
    rollen = models.CharField(max_length=256)
    rol_id = models.CharField(max_length=64)
    beschikbaarheid = models.BooleanField(default=False)

    def __str__(self):
        return self.rollen

    class Meta:
        verbose_name_plural = 'rollen'

class Kerkdiensten(models.Model):
    kerk = models.ForeignKey('Kerken', default=None)
    start_time = models.DateField()
    soort_dienst = models.ForeignKey('DienstSoorten', default='kerkdienst')
    beschikbaar = models.ManyToManyField('UserRoll', default=None, blank=True, related_name='kerkdienst_beschikbaar')
    beschikbaarheid_open = models.BooleanField(default=True)
    ingeroosterd = models.ManyToManyField('UserRoll', default=None, blank=True, related_name='kerkdienst_ingeroosterd')

    def __str__(self):
        return self.kerk.kerk_naam + ', ' + self.start_time.strftime('%d %B %Y')

    class Meta:
        verbose_name_plural = 'kerkdiensten'

class DienstSoorten(models.Model):
    naam = models.CharField(max_length=256)

    def __str__(self):
        return self.naam

    class Meta:
        verbose_name_plural = 'dienstsoorten'

class Instrumenten(models.Model):
    instrument = models.CharField(max_length=256)

    def __str__(self):
        return self.instrument

    class Meta:
        verbose_name_plural = 'instrumenten'

class UserRoll(models.Model):
    user = models.ForeignKey(User)
    rol = models.ForeignKey(Rollen)
    instrument = models.ForeignKey('Instrumenten', null=True, blank=True)

    def __str__(self):
        return self.user.username + ':' + self.rol.rollen

    class Meta:
        verbose_name_plural = 'UserRoll'

class MuziekTeams(models.Model):
    team = models.CharField(max_length=256)
    leden = models.ManyToManyField('UserRoll', blank=True)

    def __str__(self):
        return self.team

    class Meta:
        verbose_name_plural = 'MuziekTeams'
