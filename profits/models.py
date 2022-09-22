from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone


class Api (models.Model):
    date = models.DateTimeField(default=timezone.now)  
    ruya = models.CharField(max_length=12, null=True, blank=True)
    karma = models.CharField(max_length=12, null=True, blank=True)
    adil = models.CharField(max_length=12, null=True, blank=True)
    taim = models.CharField(max_length=12, null=True, blank=True)
    efix = models.CharField(max_length=12, null=True, blank=True)
    ashab = models.CharField(max_length=12, null=True, blank=True)
    turkpin = models.CharField(max_length=12, null=True, blank=True)
    razer = models.CharField(max_length=12, null=True, blank=True)
    alfurat = models.CharField(max_length=12, null=True, blank=True)
    musaab = models.CharField(max_length=12, null=True, blank=True)
    abutalal = models.CharField(max_length=12, null=True, blank=True)
    kuvyet = models.CharField(max_length=12, null=True, blank=True)
    ziraat = models.CharField(max_length=12, null=True, blank=True)
    codes = models.CharField(max_length=12, null=True, blank=True)
    bayilar = models.CharField(max_length=12, null=True, blank=True)
    depts = models.CharField(max_length=12, null=True, blank=True)
    notes = models.CharField(max_length=120, null=True, blank=True)
    total = models.CharField(max_length=12, null=True, blank=True)
    

    def __str__(self):
        return str(self.date)
    
