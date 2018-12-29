from django.shortcuts import render
from host_groups.models import Host_Groups
from .forms import HostGroupsForm

# Create your views here.
def host_groups_view(request):
    host_groups = Host_Groups.objects.all()
    context = {
        'host_groups' : host_groups,
    }
    return render(request, 'host_groups_view.html', context)


def host_groups_create(request):
    form = HostGroupsForm(request.POST or None)
    if form.is_valid(): # form doğru şekilde doldu ise kaydet
        form.save()
    context = {
        'form' : form,
    }
    return render(request, 'host_groups_create.html', context)
