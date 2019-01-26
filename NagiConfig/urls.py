"""NagiConfig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from host_groups.views import *
from hosts.views import *


urlpatterns = [
    path('', home_index),
    path('admin/', admin.site.urls),
    path('host_groups_index/', host_groups_index),
    path('host_groups_create/', host_groups_create),
    path('host_groups_update/<int:id>/', host_groups_update),
    path('host_groups_delete/<int:id>/', host_groups_delete),
    path('hosts_index/', hosts_index),
    path('host_create/', host_create),
    path('host_update/<int:id>/', host_update),
    ]
