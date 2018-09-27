from django.shortcuts import render
import datetime
import requests
API_ENDPOINT = "https://api.coinmarketcap.com/v1/ticker/"


# Create your views here.


def index(request): #always 1st param is request
    data= {
        "todays_date":str(datetime.datetime.now())
    }

    return render (request,template_name='cryptoc/crypto_index.html',context=data)


def aboutus(request):
    data ={
        "guest" : "SANTOSH"
    }
    return render(request, template_name='cryptoc/about_us.html', context=data)


def contactus(request):

    data ={
        "name": "Santosh Pariyar",
        "mob_no": ["98437*****","014*****"],
        "address":"Kathmandu"
    }
    return render(request, template_name='cryptoc/contactus.html',context=data)


def currencies(request):
    response_data = requests.get(API_ENDPOINT)
    ctx = {
        "data":response_data.json()
    }
    return render(request,template_name='cryptoc/currencies.html',context=ctx)


def git_hub(request):
    response_data = requests.get("https://api.github.com/users/hisanto")
    ctx = {
        "data":response_data.json()
    }
    return render(request,template_name='cryptoc/github.html',context=ctx)
