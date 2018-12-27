from django import forms
from .models import Host_Groups

class HostGroupsForm(forms.ModelForm):

    class Meta:
        model = Host_Groups
        fields = [
            'hostgroup_name',
            'alias',            
        ]
