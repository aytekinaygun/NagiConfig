from django import forms
from .models import Host_Groups
from django.core.exceptions import ValidationError

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

    # Girilen değerler kısıtlara göre kontrol edilir.
    def clean(self):
        hostgroup_name = self.cleaned_data.get('hostgroup_name')
        if hostgroup_name == 'a':
            raise ValidationError(('..... Hatası oldu'), code='invalid')

        return super(HostGroupsForm, self).clean()
