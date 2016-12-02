from django.contrib.auth.models import User
from django.db import models


class User_details(models.Model):
    user = models.ForeignKey(User, default=1)
    kerk = models.ForeignKey('Kerken', default=None)
    rollen = models.CharField(max_length=64)
    rollen_v2 = models.ManyToManyField('Rollen', blank=True)

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
    beschikbaar = models.ManyToManyField(User, blank=True)

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