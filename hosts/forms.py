from django import forms
from .models import Hosts
from host_groups.models import Host_Groups
from django.core.exceptions import ValidationError

class HostsForm(forms.ModelForm):

    # Parent seçeneklerinde host'un kendisi olmamalı.
    # Update formundan gelen self.instance.id = hostun id'si. queryset'de bu id hariç tutuldu.
    # view'den gelen ID'yi görmek için bu fonksiyon gerekli.
    #
    # Yeni kayıt olduğunda self.instance.id = None değerini alıyor, dolayısıyla
    # hiçbir kayıt hariç tutulmadan tüm kayıtlar geliyor. if sorgusuna gerek yok.
    def __init__(self, *args, **kwargs):
        super(HostsForm, self).__init__(*args, **kwargs)
        self.fields['parents'] = forms.ModelMultipleChoiceField(
            queryset=Hosts.objects.exclude(id=self.instance.id).order_by('host_name'),
            to_field_name='id',
            widget=forms.SelectMultiple(attrs={'class': 'form-control select2', 'data-placeholder': '  Seçiniz'}),
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
            'is_active',
            'host_name',
            'alias',
            'address',
            'parents',
            'hostgroups',
        ]
        widgets = {
            'is_active': forms.CheckboxInput(attrs={'class': 'onoffswitch-checkbox', 'id': 'myonoffswitch'}),
            'host_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: linux_sunucu'}),
            'alias': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: Linux Sunucular'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Örn: 192.168.0.1'}),
        }

    # Girilen değerler kısıtlara göre kontrol edilir.
    def clean(self):
        h_error = 0
        host_name = self.cleaned_data.get('host_name')
        print(host_name)
        # ascii karakterler dışında hata (türkçe karakteler ascii kod 128'den büyük)
        for i in host_name:
            if ord(i) >= 128:
                h_error = 1
        # Tire, harf ve sayı dışında hata
        if not host_name.replace('-', '').isalnum():
            h_error = 1
        if h_error == 1:
            raise ValidationError(('Host adı kurallara uygun değil!'), code='invalid')

        alias_error = 0
        alias = self.cleaned_data.get('alias')
        for i in alias:
            if ord(i) >= 128:
                alias_error = 1
        # Tire, boşluk, harf ve sayı dışında hata
        if not alias.replace('-', '').replace(' ', '').isalnum():
            alias_error = 1
        if alias_error == 1:
            raise ValidationError(('Host açıklaması kurallara uygun değil!'), code='invalid')

        return super(HostsForm, self).clean()
