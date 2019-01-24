# Generated by Django 2.1.4 on 2019-01-24 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('host_groups', '0003_auto_20190124_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hosts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=50, verbose_name='Host Adı')),
                ('alias', models.CharField(max_length=150, verbose_name='Host Açıklaması')),
                ('address', models.GenericIPAddressField(verbose_name='IP Adresi')),
                ('hostgroups', models.ManyToManyField(to='host_groups.Host_Groups', verbose_name='Host Grubu')),
            ],
        ),
    ]
