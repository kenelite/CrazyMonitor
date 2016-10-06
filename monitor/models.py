# -*- coding: utf-8 -*-


from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ServiceIndex(models.Model):
    name = models.CharField(max_length=64)
    key = models.CharField(max_length=64)
    data_type_choices = (
        ('int',"int"),
        ('float',"float"),
        ('str',"string")
    )

    data_type = models.CharField(u'指标数据类型', max_length=32,choices=data_type_choices,default='n/a')
    memo = models.CharField(u'备注',max_length=128,blank=True,null=True)
    def __unicode__(self):
        return "%s.%s"  %(self.name, self.key)


class Service(models.Model):
    name = models.CharField(u'服务名菜', max_length=64,unique=True)
    interval = models.IntegerField(u'监控间隔',default=60)
    plugin_name = models.CharField(u'插件名', max_length=64,default='n/a')
    items = models.ManyToManyField('ServiceIndex',verbose_name=u'指标列表',blank=True)
    memo = models.CharField(u'备注',max_length=128,blank=True,null=True)

    def __unicode__(self):
        return self.name

    #def get_service_items(obj):
    #    return ".".join([i.name for i in obj.items.all()])




class Template(models.Model):
    name = models.CharField(u'模板名称',max_length=64,unique=True)
    services = models.ManyToManyField('Service',verbose_name=u'服务列表')
    triggers = models.ManyToManyField('Trigger',verbose_name=u'触发器列表',blank=True)
    def __unicode__(self):
        return self.name


class Trigger(models.Model):
    name = models.CharField(u'触发器名称',max_length=64)
    expression = models.TextField(u'表达式')
    severity_chioces = (
        (1, 'Information'),
        (2, 'Warning'),
        (3, 'Average'),
        (4, 'High'),
        (5, 'Diaster'),
    )
    severity = models.IntegerField(u'告警级别', choices=severity_chioces)
    enabled = models.BooleanField(default=True)
    memo = models.TextField(u'备注',blank=True,null=True)
    def __unicode__(self):
        return self.name


class Host(models.Model):
    name = models.CharField(max_length=64, unique=True)
    ip_addr = models.GenericIPAddressField(unique=True)
    host_groups = models.ManyToManyField('HostGroup', blank=True)
    templates = models.ManyToManyField("Template",blank=True)
    monitored_by_choices = (
        ('agent','Agent'),
        ('snmp','SNMP'),
        ('wget','WGET'),
    )

    monitored_by = models.CharField(u'监控方式', max_length=64, choices=monitored_by_choices)
    status_choices = (
        (1,'Online'),
        (2,'Down'),
        (3,'Unreachable'),
        (4,'Offline'),
    )

    status = models.IntegerField(u'状态', choices=status_choices,default=1)
    memo = models.TextField(u'备注',blank=True,null=True)


    def __unicode__(self):
        return self.name


class HostGroup(models.Model):
    name = models.CharField(max_length=64,unique=True)
    templates = models.ManyToManyField("Template",blank=True)
    memo = models.TextField(u'备注',blank=True,null=True)

    def __unicode__(self):
        return self.name


class Action(models.Model):
    name = models.CharField(max_length=64, unique=True)
    host_groups = models.ManyToManyField('HostGroup',blank=True,)
    hosts = models.ManyToManyField('Host',blank=True)

    conditions = models.TextField(u'告警条件')
    interval = models.IntegerField(u'告警间隔(s)', default=300)
    operations = models.ManyToManyField('ActionOperation')

    recover_notice = models.BooleanField(u'故障恢复后发送通知消息',default=True)
    recover_subject = models.CharField(max_length=128, blank=True,null=True)
    recover_message = models.TextField(blank=True,null=True)

    enabled = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class ActionOperation(models.Model):
    name = models.CharField(max_length=64)
    step = models.SmallIntegerField(u'第n次告警',default=1)
    action_type_choices = (
        ('email','Email'),
        ('sms','SMS'),
        ('script', 'RunScript'),
    )

    action_type = models.CharField(u'动作类型', choices=action_type_choices,default='email',max_length=300)
    #notifiers = models.ManyToManyField(host_models.UserProfile, verbose_name=u'通知对象',blank=True)

    def __unicode__(self):
        return self.name


class Maintenance(models.Model):
    name = models.CharField(max_length=64,unique=True)
    hosts = models.ManyToManyField('Host', blank=True)
    host_group = models.ManyToManyField('HostGroup',blank=True)
    content = models.TextField(u'维护内容')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __unicode__(self):
        return self.name