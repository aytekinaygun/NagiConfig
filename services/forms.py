from django import forms
from .models import ServiceTemplate, Services
from hosts.models import Hosts

class ServiceTemplateForm(forms.ModelForm):

    class Meta:
        model = ServiceTemplate
        fields = [
            'service_description',
            'check_command',
        ]
        widgets = {
            'service_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: HTTP Web Servis Port:80'}),
            'check_command': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: check_tcp!80'}),
        }


# Servisler
####################################
class ServiceForm(forms.ModelForm):

    template = forms.ModelChoiceField(
    to_field_name='id',
    widget=forms.Select(attrs={'class': 'form-control  select2', 'data-placeholder': '  Servis şablonu seçiniz...'}),
    queryset=ServiceTemplate.objects.all().order_by('service_description'),
    label='Servis Şablonu',
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
            'template',
            'hosts',
        ]
