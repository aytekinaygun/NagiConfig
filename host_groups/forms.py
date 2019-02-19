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
        hg_error = 0
        hostgroup_name = self.cleaned_data.get('hostgroup_name')
        # ascii karakterler dışında hata (türkçe karakteler ascii kod 128'den büyük)
        for i in hostgroup_name:
            if ord(i) >= 128:
                hg_error = 1
        # Tire, harf ve sayı dışında hata
        if not hostgroup_name.replace('-', '').isalnum():
            hg_error = 1
        if hg_error == 1:
            raise ValidationError(('Host grubu adı kurallara uygun değil!'), code='invalid')

        alias_error = 0
        alias = self.cleaned_data.get('alias')
        for i in alias:
            if ord(i) >= 128:
                alias_error = 1
        # Tire, boşluk, harf ve sayı dışında hata
        if not alias.replace('-', '').replace(' ', '').isalnum():
            alias_error = 1
        if alias_error == 1:
            raise ValidationError(('Host grubu açıklaması kurallara uygun değil!'), code='invalid')

        return super(HostGroupsForm, self).clean()
