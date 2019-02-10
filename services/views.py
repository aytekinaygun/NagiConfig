from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from services.models import ServiceCommand, Services
from .forms import ServiceCommandForm, ServiceForm
from hosts.models import Hosts

# Servis Şablonu
@login_required()
def service_command_index(request):
        service_command = ServiceCommand.objects.all()
        context = {
            'service_command' : service_command,
            'title'           : 'Servis Komutları',
            }
        return render(request, 'service_command_index.html', context)

@login_required()
def service_command_create(request):
    form = ServiceCommandForm(request.POST or None)
    if form.is_valid():
        sc = form.save()
        messages.success(request, 'Yeni kayıt başarılı.', extra_tags='alert-success')
        return redirect('/service_command_index/') # kayıtdan sonra buraya dön
    context = {
        'form' : form,
        'title': 'Yeni Servis Komutu Oluştur',
        }
    return render(request, 'service_command_form.html', context)

@login_required()
def service_command_update(request, id):
    update = "yes" # sil butonu olmaması için.
    cmd_name = get_object_or_404(ServiceCommand, id=id)
    form = ServiceCommandForm(request.POST or None, instance=cmd_name) # formu doldur
    if form.is_valid():
        form.save()
        messages.success(request, 'Güncelleme başarılı.', extra_tags='alert-success')
        return redirect('/service_command_index/') # kayıtdan sonra buraya dön
    context = {
        'form'   : form,
        'title'  : 'Servis Şablonunu Güncelle',
        'update' : 'yes',
        'id'     : id,
        }
    return render(request, 'service_command_form.html', context)

@login_required()
def service_command_delete(request, id):
    cmd_name = get_object_or_404(ServiceCommand, id=id)
    cmd_name.delete()
    messages.success(request, 'Silme başarılı.', extra_tags='alert-success')
    return redirect('/service_command_index/')


# Servis
##############################################
@login_required()
def services_index(request):
        services = Services.objects.all()
        hosts = Hosts.objects.all()
        context = {
            'services' : services,
            'hosts'    : hosts,
            'title'    : 'Servisler',
            }
        return render(request, 'services_index.html', context)

@login_required()
def service_create(request):
    form = ServiceForm(request.POST or None)
    if form.is_valid():
        s = form.save()
        messages.success(request, 'Yeni kayıt başarılı.', extra_tags='alert-success')
        return redirect('/services_index/') # kayıtdan sonra buraya dön
    context = {
        'form' : form,
        'title': 'Yeni Servis Ekle',
        }
    return render(request, 'service_form.html', context)

@login_required()
def service_update(request, id):
    update = "yes" # sil butonu olmaması için.
    s = get_object_or_404(Services, id=id)
    form = ServiceForm(request.POST or None, instance=s) # formu doldur
    if form.is_valid():
        form.save()
        messages.success(request, 'Güncelleme başarılı.', extra_tags='alert-success')
        return redirect('/services_index/') # kayıtdan sonra buraya dön
    context = {
        'form'   : form,
        'title'  : 'Servis Güncelle',
        'update' : 'yes',
        'id'     : id,
        }
    return render(request, 'service_form.html', context)

@login_required()
def service_delete(request, id):
    s = get_object_or_404(Services, id=id)
    s.delete()
    messages.success(request, 'Silme başarılı.', extra_tags='alert-success')
    return redirect('/services_index/')
