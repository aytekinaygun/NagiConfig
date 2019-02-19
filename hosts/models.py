from django.db import models
from django.core.exceptions import ValidationError

help_text_1 = 'Türkçe karakter kullanmayınız. Sadece harf, sayı ve tire (-) içerebilir.'
help_text_2 = 'Türkçe karakter kullanmayınız. Sadece harf, sayı, boşluk ve tire (-) içerebilir.'

# Create your models here.
class Hosts(models.Model):
    host_name = models.CharField(max_length=50, verbose_name='Host Adı', help_text=help_text_1, unique=True) # unique=benzersiz
    alias = models.CharField(max_length=150, verbose_name='Host Açıklaması', help_text=help_text_2)
    address = models.GenericIPAddressField(verbose_name='IP Adresi')
    parents = models.ManyToManyField('Hosts')
    hostgroups = models.ManyToManyField('host_groups.Host_Groups')
    is_active = models.BooleanField(default=False, verbose_name='')

    # Admin panelde listede grup adı görünür.
    def __str__(self):
        return self.host_name

    # Girilen değerler kısıtlara göre kontrol edilir.
    # def clean(self):
    #     for parent in self.parents.all():
    #         if self.id == parent.id:
    #             print(self.id, parent.id)
    #             raise ValidationError(('..... aynı host olamaz.'), code='invalid')
