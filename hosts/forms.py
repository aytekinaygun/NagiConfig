from django import forms
from .models import Hosts
from host_groups.models import Host_Groups

class HostsForm(forms.ModelForm):

    class Meta:
        model = Hosts
        fields = [
            'host_name',
            'alias',
            'address',
            'hostgroups',
        ]
        widgets = {
            'host_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: linux_sunucu'}),
            'alias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: Linux Sunucular'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: Linux Sunucular'}),
            'hostgroups': forms.ModelMultipleChoiceField(queryset=Host_Groups.objects.all()),
        }
