# Generated by Django 2.1.4 on 2019-01-24 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host_groups', '0002_auto_20190124_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hosts',
            name='hostgroups',
        ),
        migrations.DeleteModel(
            name='Hosts',
        ),
    ]
