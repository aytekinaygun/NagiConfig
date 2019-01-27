from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from hosts.models import Hosts
from .forms import HostsForm
from host_groups.models import Host_Groups

def hosts_index(request):
    hosts = Hosts.objects.all()
    hostgroups = Host_Groups.objects.all()
    context = {
        'hosts'     : hosts,
        'hostgroups': hostgroups,
        'title'     : 'Hostlar',
        }
    return render(request, 'hosts_index.html', context)

def host_create(request):
    form = HostsForm(request.POST or None)
    if form.is_valid(): # form doğru şekilde doldu ise kaydet
        h = form.save()
        messages.success(request, 'Yeni kayıt başarılı.', extra_tags='alert-success')
        return redirect('/hosts_index/') # kayıtdan sonra buraya dön
    context = {
        'form' : form,
        'title': 'Yeni Host Oluştur',
        }
    return render(request, 'hosts_form.html', context)

def host_update(request, id):
    update = "yes" # sil butonu olmaması için.
    h = get_object_or_404(Hosts, id=id)
    form = HostsForm(request.POST or None, instance=h) # formu doldur
    if form.is_valid(): # form doğru şekilde doldu ise kaydet
        form.save()
        messages.success(request, 'Güncelleme başarılı.', extra_tags='alert-success')
        return redirect('/hosts_index/') # kayıtdan sonra buraya dön
    context = {
        'form'   : form,
        'title'  : 'Host Bilgisini Güncelle',
        'update' : 'yes',
        'id'     : id,
        }
    return render(request, 'hosts_form.html', context)
