from django.shortcuts import render, get_object_or_404, redirect
from hosts.models import Hosts
from host_groups.models import Host_Groups
from services.models import Services
from django.db.models import Count # group_by_host_groups


def home_index(request):
    count_hosts          = Hosts.objects.count()
    count_host_groups    = Host_Groups.objects.count()
    count_services       = Services.objects.count()
    group_by_host_groups = Hosts.objects.values('hostgroups').annotate(total=Count('hostgroups')).order_by('hostgroups')
    hostgroups           = Host_Groups.objects.all()

    # Sözlükde hostgroup id bilgisi hostgroup_name ile değiştirilir.
    for hg in group_by_host_groups:
        id = hg['hostgroups']
        hg_name = Host_Groups.objects.get(id=id)
        hg['hostgroups'] = hg_name.hostgroup_name

    context = {
        'count_hosts'          : count_hosts,
        'count_host_groups'    : count_host_groups,
        'count_services'       : count_services,
        'group_by_host_groups' : group_by_host_groups,
        'hostgroups'           : hostgroups,
        'xxx'                  : ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
        }
    return render(request, 'home.html', context)
