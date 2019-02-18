from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Host_Groups(models.Model):
    hostgroup_name = models.CharField(
    max_length=50,
    verbose_name='Host Grubu Adı',
    help_text='Türkçe karakter kullanmayınız. Sadece harf, sayı ve tire (-) içerebilir.',
    unique=True
    )
    alias = models.CharField(
    max_length=150,
    help_text='Türkçe karakter kullanmayınız. Sadece harf, sayı, boşluk ve tire (-) içerebilir.',
    verbose_name='Host Grubu Açıklaması'
    )

    # Admin panelde listede grup adı görünür.
    def __str__(self):
        return self.hostgroup_name
