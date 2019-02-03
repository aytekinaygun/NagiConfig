from django.db import models
from django.core.exceptions import ValidationError

class ServiceTemplate(models.Model):
    service_description = models.CharField(
        max_length=150, verbose_name='Servis Açıklaması',
        help_text='Türkçe karakter kullanmayınız. Harf, sayı, boşluk, tire (-) ve iki nokta üstüste (:) içerebilir.',
        unique=True
        )
    check_command = models.CharField(max_length=150, verbose_name='Servis Komutu')

    def __str__(self):
        return self.service_description


class Services(models.Model):
    template = models.ForeignKey('ServiceTemplate', on_delete=models.CASCADE)
    hosts = models.ManyToManyField('hosts.Hosts')
