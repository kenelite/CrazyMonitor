# -*- coding: utf-8 -*-


class ServiceItem(models.Model):
    name = models.CharField(u'指标名称',max_length=64,blank=True,null=True)
    item_key = models.CharField(u'服务指标key',max_length=64)
    data_type_choices = (
        ('int', "int"),
        ('float', "float"),
        ('str', "string")
    )

    data_type = models.CharField(u'指标数据类型',max_length=32,choices=data_type_choices,default='n/a')
    memo = models.CharField(u'备注',max_length=128,blank=True,null=True)
    def __unicode__(self):
        return "%s.%s" %(self.name,self.item_key)
