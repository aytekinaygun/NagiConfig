from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Hosts(models.Model):
    host_name = models.CharField(max_length=50, verbose_name='Host Adı')
    alias = models.CharField(max_length=150, verbose_name='Host Açıklaması')
    address = models.GenericIPAddressField(verbose_name='IP Adresi')
    hostgroups = models.ManyToManyField('host_groups.Host_Groups', verbose_name='Host Grubu')
