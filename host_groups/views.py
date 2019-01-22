from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from host_groups.models import Host_Groups
from .forms import HostGroupsForm

def host_groups_index(request):
    host_groups = Host_Groups.objects.all()
    context = {
        'host_groups' : host_groups,
        'title' : 'Host Grupları',
    }
    return render(request, 'host_groups_index.html', context)


def host_groups_create(request):
    form = HostGroupsForm(request.POST or None)
    if form.is_valid(): # form doğru şekilde doldu ise kaydet
        hg = form.save()
        messages.success(request, 'Yeni kayıt başarılı.', extra_tags='alert-success')
        return redirect('/host_groups_index/') # kayıtdan sonra buraya dön
    context = {
        'form' : form,
        'title': 'Yeni Host Grubu Oluştur',
    }
    return render(request, 'host_group_form.html', context)


def host_groups_update(request, id):
    hg = get_object_or_404(Host_Groups, id=id)
    form = HostGroupsForm(request.POST or None, instance=hg) # formu doldur
    if form.is_valid(): # form doğru şekilde doldu ise kaydet
        form.save()
        messages.success(request, 'Güncelleme başarılı.', extra_tags='alert-success')
        return redirect('/host_groups_index/') # kayıtdan sonra buraya dön
    context = {
        'form'   : form,
        'title'  : 'Host Grubunu Güncelle',
        'update' : 'yes'
    }
    return render(request, 'host_group_form.html', context)


def host_groups_delete(request, id):
    hg = get_object_or_404(Host_Groups, id=id)
    hg.delete()
    messages.success(request, 'Silme başarılı.')
    return redirect('/host_groups_index/')
