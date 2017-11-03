# from django.shortcuts import render
from django.http import HttpResponse
import os
import requests


# Create your views here.
def index(request):
    do_token = os.getenv("DIGITALOCEAN_API_TOKEN") 
    if do_token is not None:
        do_api_url = 'https://api.digitalocean.com/v2/droplets'
        headers = {'Authorization': 'Bearer {}'.format(do_token)}
        r = requests.get(do_api_url, headers=headers)

        return HttpResponse("{}".format(r.text))

    else:
        return HttpResponse("vmdash: DIGITALOCEAN_API_TOKEN needs to be defined")
