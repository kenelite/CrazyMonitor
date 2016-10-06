from django.conf.urls import url

import  views

urlpatterns = [

    url(r'client/config/(\d+)/$',views.client_configs )


]
