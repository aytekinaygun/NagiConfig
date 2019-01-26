from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Host_Groups(models.Model):
    hostgroup_name = models.CharField(max_length=50, verbose_name='Host Grubu Adı')
    alias = models.CharField(max_length=150, verbose_name='Host Grubu Açıklaması')

    # Admin panelde listede grup adı görünür.  
    def __str__(self):
        return self.hostgroup_name

    # Girilen değerler kısıtlara göre kontrol edilir.
    def clean(self):
        if self.hostgroup_name == 'a':
            raise ValidationError(('budur'), code='invalid')
