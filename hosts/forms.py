from django import forms
from .models import Hosts
from host_groups.models import Host_Groups

class HostsForm(forms.ModelForm):
    hostgroups = forms.ModelMultipleChoiceField(
        to_field_name='id',
        widget=forms.SelectMultiple(attrs={'class': 'form-control select2', 'data-placeholder': '  Grup seçiniz...'}),
        queryset=Host_Groups.objects.all(),
        # queryset=Host_Groups.objects.all().values_list('hostgroup_name', flat=True), # flat True olmaz ise grup adı parantezli ve tırnak içinde geliyor.
        label='Host Grubu',
        )

    # def __init__(self, *args, **kwargs):
    #     super(HostsForm, self).__init__(*args, **kwargs)
    #
    #     self.fields['hostgroups'].queryset = Host_Groups.objects.all()#.values_list('id','hostgroup_name')

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
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: 192.168.0.1'}),
        }
