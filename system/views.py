from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from host_groups.models import Host_Groups
from hosts.models import Hosts
from services.models import Services, ServiceCommand

@login_required()
def system(request):
    context = {}
    return render(request, 'system.html', context)

@login_required()
def nagios_restart(request):
    # Define Host Groups
    # -------------------------------------
    hostgroups = Host_Groups.objects.all()
    f = open('nc-hostgroups.cfg', 'w')
    for hg in hostgroups:
        f.write('define hostgroup{\n')
        f.write('   hostgroup_name  %s\n' % (hg.hostgroup_name))
        f.write('   alias           %s\n' % (hg.alias))
        f.write('}\n')
    f.close()

    # Define Hosts
    # -------------------------------------
    hosts = Hosts.objects.all()
    f = open('nc-hosts.cfg', 'w')
    for h in hosts:
        f.write('define host{\n')
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
            hg_list = hg_list + hg.hostgroup_name + ' '
        hg_list = hg_list.strip().replace(' ', ', ')
        if hg_list != '':
            f.write('   hostgroups  %s\n' % (hg_list))

        f.write('}\n')
    f.close()

    # Define Services
    # -------------------------------------
    services = Services.objects.exclude(hosts__isnull=True) # host ilişkisi boş olmayanlar

    f = open('nc-services.cfg', 'w')
    for s in services:
        f.write('define service{\n')
        f.write('   service_description %s\n' % (s.service_description))

        # Hosts
        h_list = ''
        for h in s.hosts.all():
            h_list = h_list + h.host_name + ' '
        h_list = h_list.strip().replace(' ', ', ')
        f.write('   host_name   %s\n' % (h_list))

        cmd = ServiceCommand.objects.get(id=s.service_description_id)
        f.write('   check_command   %s\n' % (cmd.check_command))

        f.write('}\n')
    f.close()




    messages.success(request, 'Nagios tekrar başlatıldı.', extra_tags='alert-success')
    return redirect('/system/')
