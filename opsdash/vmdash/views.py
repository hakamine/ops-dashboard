from django.shortcuts import render
from django.http import HttpResponse
import os

# not using digitalocean module for now, it doesn't seem to be of much help
# import digitalocean
import ovh
import requests


# Create your views here.

def index(request):
    return render(request, 'vmdash/index.html')

# not using the digitalocean library
# def digital_ocean_library(request):
#     do_token = os.getenv("DIGITALOCEAN_API_TOKEN")
#     if do_token is not None:
#         manager = digitalocean.Manager(token=do_token)
#         my_droplets = manager.get_all_droplets()
#         return HttpResponse("droplets: {} {}".format(len(my_droplets), str(my_droplets)))
#     else:
#         return HttpResponse("vmdash: DIGITALOCEAN_API_TOKEN needs to be defined")


def digital_ocean_droplets(request):
    do_token = os.getenv("DIGITALOCEAN_API_TOKEN")
    if do_token is not None:
        do_api_url = 'https://api.digitalocean.com/v2/droplets'
        headers = {'Authorization': 'Bearer {}'.format(do_token)}
        r = requests.get(do_api_url, headers=headers)

        return HttpResponse("{}".format(r.text))

    else:
        return HttpResponse("vmdash: DIGITALOCEAN_API_TOKEN needs to be defined")


def ovh_cloud_projects(request):
    # get credentials from env vars
    ovh_application_key = os.getenv("OVH_APPLICATION_KEY")
    ovh_application_secret = os.getenv("OVH_APPLICATION_SECRET")
    ovh_consumer_key = os.getenv("OVH_CONSUMER_KEY")

    client = ovh.Client(
        endpoint='ovh-ca',
        application_key=ovh_application_key,
        application_secret=ovh_application_secret,
        consumer_key=ovh_consumer_key,
    )

    # The API call /cloud/project gets a list of project ids only
    resp = client.get('/cloud/project')

    return HttpResponse("{}".format(resp))
