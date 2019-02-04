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
    # group_by_host_groups = Host_Groups.objects.values('hostgroup_name').annotate(total=Count('hostgroup_name')).order_by('hostgroup_name')
    print(group_by_host_groups)
    context = {
        'count_hosts'          : count_hosts,
        'count_host_groups'    : count_host_groups,
        'count_services'       : count_services,
        'group_by_host_groups' : group_by_host_groups,
        'hostgroups'           : hostgroups,
        }
    return render(request, 'home.html', context)
