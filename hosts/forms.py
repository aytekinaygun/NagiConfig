from django import forms
from .models import Hosts
from host_groups.models import Host_Groups

class HostsForm(forms.ModelForm):
    parents = forms.ModelMultipleChoiceField(
    to_field_name='id',
    widget=forms.SelectMultiple(attrs={'class': 'form-control select2', 'data-placeholder': '  Seçiniz'}),
    queryset=Hosts.objects.all().order_by('host_name'),
    label='Bağlı Olduğu Host(lar)',
    )

    hostgroups = forms.ModelMultipleChoiceField(
        to_field_name='id',
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2', 'data-placeholder': '  Birden fazla grup seçebilirsiniz...'}),
        queryset=Host_Groups.objects.all().order_by('hostgroup_name'),
        label='Üyesi Olduğu Host Grubu',
    )

    class Meta:
        model = Hosts
        fields = [
            'host_name',
            'alias',
            'address',
            'parents',
            'hostgroups',
        ]
        widgets = {
            'host_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: linux_sunucu'}),
            'alias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: Linux Sunucular'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: 192.168.0.1'}),
        }
