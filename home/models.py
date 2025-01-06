# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Board(models.Model):

    #__Board_FIELDS__
    boardid = models.TextField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Board_FIELDS__END

    class Meta:
        verbose_name        = _("Board")
        verbose_name_plural = _("Board")


class Player(models.Model):

    #__Player_FIELDS__
    playerid = models.TextField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)

    #__Player_FIELDS__END

    class Meta:
        verbose_name        = _("Player")
        verbose_name_plural = _("Player")


class Tournament_Type(models.Model):

    #__Tournament_Type_FIELDS__
    toernamenttypeid = models.TextField(max_length=255, null=True, blank=True)
    name = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)
    legspoints = models.IntegerField(null=True, blank=True)
    matchpoints = models.IntegerField(null=True, blank=True)
    format = models.TextField(max_length=255, null=True, blank=True)
    setslegs = models.TextField(max_length=255, null=True, blank=True)
    bestof = models.IntegerField(null=True, blank=True)

    #__Tournament_Type_FIELDS__END

    class Meta:
        verbose_name        = _("Tournament_Type")
        verbose_name_plural = _("Tournament_Type")


class Tournament(models.Model):

    #__Tournament_FIELDS__
    tournamentid = models.TextField(max_length=255, null=True, blank=True)
    tournamenttypeid = models.ForeignKey(tournament_type, on_delete=models.CASCADE)
    rounds = models.IntegerField(null=True, blank=True)
    startdate = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Tournament_FIELDS__END

    class Meta:
        verbose_name        = _("Tournament")
        verbose_name_plural = _("Tournament")


class Participants(models.Model):

    #__Participants_FIELDS__
    playerid = models.ForeignKey(player, on_delete=models.CASCADE)
    tournamentid = models.ForeignKey(tournament, on_delete=models.CASCADE)

    #__Participants_FIELDS__END

    class Meta:
        verbose_name        = _("Participants")
        verbose_name_plural = _("Participants")


class Game(models.Model):

    #__Game_FIELDS__
    gamename = models.TextField(max_length=255, null=True, blank=True)
    homename = models.ForeignKey(player, on_delete=models.CASCADE)
    awayname = models.ForeignKey(player, on_delete=models.CASCADE)
    boardid = models.ForeignKey(board, on_delete=models.CASCADE)
    tournamentid = models.ForeignKey(tournament, on_delete=models.CASCADE)
    homescore = models.IntegerField(null=True, blank=True)
    awayscore = models.IntegerField(null=True, blank=True)

    #__Game_FIELDS__END

    class Meta:
        verbose_name        = _("Game")
        verbose_name_plural = _("Game")



#__MODELS__END
