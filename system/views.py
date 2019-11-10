from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from host_groups.models import Host_Groups
from hosts.models import Hosts
from services.models import Services, ServiceCommand
import os

@login_required()
def system(request):
    context = {}
    return render(request, 'system.html', context)

@login_required()
def nagios_restart(request):
    # Define Host Groups
    # -------------------------------------
    hostgroups = Host_Groups.objects.all()
    f = open('conf.d/nc-hostgroups.cfg', 'w')
    for hg in hostgroups:
        f.write('define hostgroup{\n')
        f.write('   hostgroup_name  %s\n' % ('grup-' + hg.hostgroup_name))
        f.write('   alias           %s\n' % (hg.alias))
        f.write('}\n')
    f.close()

    # Define Hosts
    # -------------------------------------
    hosts = Hosts.objects.filter(is_active=True)
    f = open('conf.d/nc-hosts.cfg', 'w')
    for h in hosts:
        f.write('define host{\n')
        f.write('   use         windows-server\n')
        f.write('   host_name   %s\n' % (h.host_name))
        f.write('   alias       %s\n' % (h.alias))
        f.write('   address     %s\n' % (h.address))
        # parents
        p_list = ''
        for ho in h.parents.all():
            p_list = p_list + ho.host_name + ' '
        p_list = p_list.strip().replace(' ', ', ')
        if p_list != '':
            f.write('   parents     %s\n' % (p_list))
        # hostgroups
        hg_list = ''
        for hg in h.hostgroups.all():
            hg_list = hg_list + 'grup-' + hg.hostgroup_name + ' '
        hg_list = hg_list.strip().replace(' ', ', ')
        if hg_list != '':
            f.write('   hostgroups  %s\n' % (hg_list))
        f.write('}\n')
    f.close()

    # Define Services
    # -------------------------------------
    services = Services.objects.exclude(hosts__isnull=True) # host ilişkisi boş olmayanlar
    f = open('conf.d/nc-services.cfg', 'w')
    for s in services:
        success = 1
        define =  ('define service{\n')
        define += ('   use  generic-service\n')
        define += ('   service_description %s\n' % (s.service_description))
        # Hosts
        h_list = ''
        for h in s.hosts.filter(is_active=True):
            h_list += h.host_name + ' '
        h_list = h_list.strip().replace(' ', ', ')
        if h_list == '':
            success = 0
        define += ('   host_name   %s\n' % (h_list))
        cmd = ServiceCommand.objects.get(id=s.service_description_id)
        define += ('   check_command   %s\n' % (cmd.check_command))
        define += ('}\n')
        if success == 1:
            f.write(define)
    f.close()

    os.system('systemctl restart nagios4.service')

    messages.success(request, 'Nagios tekrar başlatıldı.', extra_tags='alert-success')
    return redirect('/system/')
