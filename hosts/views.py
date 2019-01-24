from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from hosts.models import Hosts
from .forms import HostsForm

def hosts_index(request):
    hosts = Hosts.objects.all()
    context = {
        'hosts' : hosts,
        'title' : 'Hostlar',
        }
    return render(request, 'hosts_index.html', context)

def hosts_create(request):
    form = HostsForm(request.POST or None)
    if form.is_valid(): # form doğru şekilde doldu ise kaydet
        hg = form.save()
        messages.success(request, 'Yeni kayıt başarılı.', extra_tags='alert-success')
        return redirect('/hosts_index/') # kayıtdan sonra buraya dön
    context = {
        'form' : form,
        'title': 'Yeni Host Oluştur',
        }
    return render(request, 'hosts_form.html', context)
