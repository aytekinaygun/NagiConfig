from django.db import models

# Create your models here.
class Host_Groups(models.Model):
    hostgroup_name = models.CharField(max_length=50, verbose_name="Host Grubu Adı")
    alias = models.CharField(max_length=150)
