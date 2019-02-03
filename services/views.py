from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from services.models import ServiceTemplate, Services
from .forms import ServiceTemplateForm, ServiceForm
from hosts.models import Hosts

# Servis Şablonu
def services_template_index(request):
        services_template = ServiceTemplate.objects.all()
        context = {
            'services_template'     : services_template,
            'title'                 : 'Servis Şablonları',
            }
        return render(request, 'services_template_index.html', context)

def service_template_create(request):
    form = ServiceTemplateForm(request.POST or None)
    if form.is_valid():
        h = form.save()
        messages.success(request, 'Yeni kayıt başarılı.', extra_tags='alert-success')
        return redirect('/services_template_index/') # kayıtdan sonra buraya dön
    context = {
        'form' : form,
        'title': 'Yeni Servis Şablonu Oluştur',
        }
    return render(request, 'service_template_form.html', context)

def service_template_update(request, id):
    update = "yes" # sil butonu olmaması için.
    template = get_object_or_404(ServiceTemplate, id=id)
    form = ServiceTemplateForm(request.POST or None, instance=template) # formu doldur
    if form.is_valid():
        form.save()
        messages.success(request, 'Güncelleme başarılı.', extra_tags='alert-success')
        return redirect('/services_template_index/') # kayıtdan sonra buraya dön
    context = {
        'form'   : form,
        'title'  : 'Servis Şablonunu Güncelle',
        'update' : 'yes',
        'id'     : id,
        }
    return render(request, 'service_template_form.html', context)

def service_template_delete(request, id):
    template = get_object_or_404(ServiceTemplate, id=id)
    template.delete()
    messages.success(request, 'Silme başarılı.', extra_tags='alert-success')
    return redirect('/services_template_index/')


# Servis
##############################################
def services_index(request):
        services = Services.objects.all()
        hosts = Hosts.objects.all()
        context = {
            'services' : services,
            'hosts'    : hosts,
            'title'    : 'Servisler',
            }
        return render(request, 'services_index.html', context)

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

def service_delete(request, id):
    s = get_object_or_404(Services, id=id)
    s.delete()
    messages.success(request, 'Silme başarılı.', extra_tags='alert-success')
    return redirect('/services_index/')
