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
    # Yukarıdaki sorgudan gelen veri:
    # [{'hostgroups':1, total:5}, {'hostgroups':2, total:7}]
    # 1 ve 2 hostgroups'un id'si

    myChartHostGroups_labels = []
    myChartHostGroups_data   = []
    for hg in group_by_host_groups:
        id = hg['hostgroups']
        hg_name = Host_Groups.objects.get(id=id)
        myChartHostGroups_labels.append(hg_name)
        myChartHostGroups_data.append(hg['total'])

    context = {
        'count_hosts'              : count_hosts,
        'count_host_groups'        : count_host_groups,
        'count_services'           : count_services,
        'myChartHostGroups_labels' : myChartHostGroups_labels,
        'myChartHostGroups_data'   : myChartHostGroups_data,
        }
    return render(request, 'home.html', context)
