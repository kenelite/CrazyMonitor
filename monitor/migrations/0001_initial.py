# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-06 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('conditions', models.TextField(verbose_name='\u544a\u8b66\u6761\u4ef6')),
                ('interval', models.IntegerField(default=300, verbose_name='\u544a\u8b66\u95f4\u9694(s)')),
                ('recover_notice', models.BooleanField(default=True, verbose_name='\u6545\u969c\u6062\u590d\u540e\u53d1\u9001\u901a\u77e5\u6d88\u606f')),
                ('recover_subject', models.CharField(blank=True, max_length=128, null=True)),
                ('recover_message', models.TextField(blank=True, null=True)),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ActionOperation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('step', models.SmallIntegerField(default=1, verbose_name='\u7b2cn\u6b21\u544a\u8b66')),
                ('action_type', models.CharField(choices=[('email', 'Email'), ('sms', 'SMS'), ('script', 'RunScript')], default='email', max_length=300, verbose_name='\u52a8\u4f5c\u7c7b\u578b')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('ip_addr', models.GenericIPAddressField(unique=True)),
                ('monitored_by', models.CharField(choices=[('agent', 'Agent'), ('snmp', 'SNMP'), ('wget', 'WGET')], max_length=64, verbose_name='\u76d1\u63a7\u65b9\u5f0f')),
                ('status', models.IntegerField(choices=[(1, 'Online'), (2, 'Down'), (3, 'Unreachable'), (4, 'Offline')], default=1, verbose_name='\u72b6\u6001')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('content', models.TextField(verbose_name='\u7ef4\u62a4\u5185\u5bb9')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('host_group', models.ManyToManyField(blank=True, to='monitor.HostGroup')),
                ('hosts', models.ManyToManyField(blank=True, to='monitor.Host')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='\u670d\u52a1\u540d\u83dc')),
                ('interval', models.IntegerField(default=60, verbose_name='\u76d1\u63a7\u95f4\u9694')),
                ('plugin_name', models.CharField(default='n/a', max_length=64, verbose_name='\u63d2\u4ef6\u540d')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceIndex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('key', models.CharField(max_length=64)),
                ('data_type', models.CharField(choices=[('int', 'int'), ('float', 'float'), ('str', 'string')], default='n/a', max_length=32, verbose_name='\u6307\u6807\u6570\u636e\u7c7b\u578b')),
                ('memo', models.CharField(blank=True, max_length=128, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='\u6a21\u677f\u540d\u79f0')),
                ('services', models.ManyToManyField(to='monitor.Service', verbose_name='\u670d\u52a1\u5217\u8868')),
            ],
        ),
        migrations.CreateModel(
            name='Trigger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='\u89e6\u53d1\u5668\u540d\u79f0')),
                ('expression', models.TextField(verbose_name='\u8868\u8fbe\u5f0f')),
                ('severity', models.IntegerField(choices=[(1, 'Information'), (2, 'Warning'), (3, 'Average'), (4, 'High'), (5, 'Diaster')], verbose_name='\u544a\u8b66\u7ea7\u522b')),
                ('enabled', models.BooleanField(default=True)),
                ('memo', models.TextField(blank=True, null=True, verbose_name='\u5907\u6ce8')),
            ],
        ),
        migrations.AddField(
            model_name='template',
            name='triggers',
            field=models.ManyToManyField(blank=True, to='monitor.Trigger', verbose_name='\u89e6\u53d1\u5668\u5217\u8868'),
        ),
        migrations.AddField(
            model_name='service',
            name='items',
            field=models.ManyToManyField(blank=True, to='monitor.ServiceIndex', verbose_name='\u6307\u6807\u5217\u8868'),
        ),
        migrations.AddField(
            model_name='hostgroup',
            name='templates',
            field=models.ManyToManyField(blank=True, to='monitor.Template'),
        ),
        migrations.AddField(
            model_name='host',
            name='host_groups',
            field=models.ManyToManyField(blank=True, to='monitor.HostGroup'),
        ),
        migrations.AddField(
            model_name='action',
            name='host_groups',
            field=models.ManyToManyField(blank=True, to='monitor.HostGroup'),
        ),
        migrations.AddField(
            model_name='action',
            name='hosts',
            field=models.ManyToManyField(blank=True, to='monitor.Host'),
        ),
        migrations.AddField(
            model_name='action',
            name='operations',
            field=models.ManyToManyField(to='monitor.ActionOperation'),
        ),
    ]