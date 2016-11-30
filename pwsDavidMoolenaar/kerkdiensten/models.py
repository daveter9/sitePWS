from django.contrib.auth.models import User
from django.db import models

class User_details(models.Model):
    user = models.ForeignKey(User, default=1)
    kerk = models.ForeignKey('Kerken', default=None)
    rollen = models.CharField(max_length=64)

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

    def __str__(self):
        return self.rollen

    class Meta:
        verbose_name_plural = 'rollen'