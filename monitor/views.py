from django.shortcuts import render,HttpResponse
import json
# Create your views here.

from serializer import ClientHandler



def client_configs(request, client_id):

    print("----->",client_id)
    config_obj = ClientHandler(client_id)
    config = config_obj.fetch_configs

    if config:
        return HttpResponse(json.dumps(config))
