from django.contrib import admin
from .models import Hosts

# Register your models here.
admin.site.register(Hosts, verbose_name='Hostlar')
