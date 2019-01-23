from django import forms
from .models import Host_Groups

class HostGroupsForm(forms.ModelForm):

    class Meta:
        model = Host_Groups
        fields = [
            'hostgroup_name',
            'alias',
        ]
        widgets = {
            'hostgroup_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: linux_sunucu'}),
            'alias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: Linux Sunucular'}),
        }
