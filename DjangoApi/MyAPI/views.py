from django.shortcuts import render, HttpResponse
import requests
import json

def getAPI(request):
  URL_API = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,tether,binance-coin,usd-coin&vs_currencies=usd&x_cg_demo_api_key=CG-ZmYdhwv2yEiogyRD9U7iM9tw"


  response = requests.get(URL_API)

  if response.status_code == 200:

    response_json = json.dumps(response.json())

    
    return HttpResponse(response_json, content_type="application/json")
  else:
    return HttpResponse(status=response.status_code)  # Manejar códigos de estado no 200
