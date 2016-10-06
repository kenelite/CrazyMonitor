# -*- coding: utf-8 -*-

import models
from django.core.exceptions import ObjectDoesNotExist


class ClientHandler(object):

    def __init__(self,client_id):
        self.client_id = client_id
        self.client_configs = {
            "services": {}
        }


    @property
    def fetch_configs(self):

        try:
            host_obj = models.Host.objects.get(id = self.client_id)

            template_list =  list( host_obj.templates.select_related() )


            for host_group in host_obj.host_groups.select_related():
                template_list.extend( list (host_obj.templates.select_related() ))

            print (template_list)

            for template in template_list:
                #print (template.services.select_related())

                for service in template.services.select_related():
                    self.client_configs['services'][service.name] = [ service.plugin_name,service.interval ]




        except ObjectDoesNotExist:
            pass

        return self.client_configs