from django.contrib import admin

# Register your models here.

import models


admin.site.register(models.Host)
admin.site.register(models.HostGroup)
admin.site.register(models.Template)
admin.site.register(models.ServiceIndex)
admin.site.register(models.Service)
admin.site.register(models.Trigger)
admin.site.register(models.Action)
admin.site.register(models.ActionOperation)
admin.site.register(models.Maintenance)