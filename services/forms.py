from django import forms
from .models import ServiceCommand, Services
from hosts.models import Hosts

class ServiceCommandForm(forms.ModelForm):

    class Meta:
        model = ServiceCommand
        fields = [
            'command_description',
            'check_command',
        ]
        widgets = {
            'command_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: HTTP Web Servis Port:80'}),
            'check_command': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: check_tcp!80'}),
        }


# Servisler
####################################
class ServiceForm(forms.ModelForm):

    service_description = forms.ModelChoiceField(
    to_field_name='id',
    widget=forms.Select(attrs={'class': 'form-control  select2', 'data-placeholder': '  Servis komutu seçiniz...'}),
    queryset=ServiceCommand.objects.all().order_by('command_description'),
    label='Servis Açıklaması',
    )

    hosts = forms.ModelMultipleChoiceField(
        to_field_name='id',
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2', 'data-placeholder': '  Host seçiniz...'}),
        queryset=Hosts.objects.all().order_by('host_name'),
        label='Host(lar)',
        )

    class Meta:
        model = Services
        fields = [
            'service_description',
            'hosts',
        ]
