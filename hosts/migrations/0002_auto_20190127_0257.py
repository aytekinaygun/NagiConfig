# Generated by Django 2.1.4 on 2019-01-26 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hosts',
            name='parents',
            field=models.ManyToManyField(to='hosts.Hosts'),
        ),
        migrations.AlterField(
            model_name='hosts',
            name='hostgroups',
            field=models.ManyToManyField(to='host_groups.Host_Groups'),
        ),
    ]
