# views.py
from django.http import HttpResponse
from rest_framework.decorators import api_view
import numpy as np
import datetime
import json



from src.main_handler import MainHandler

HEADERS = {
    'Access-Control-Allow-Origin': '*',
};

@api_view(['GET'])
def main(request):
    return HttpResponse("Python AI works on nginx!", headers=HEADERS)

@api_view(['GET'])
def describe_ids(request):
    ids = request.query_params.getlist('ids[]')

    description = MainHandler.get_ids_description([int(i) for i in ids])
    return HttpResponse(json.dumps(description), headers=HEADERS)

@api_view(['GET'])
# Links of resources by ids
def get_links(request):
    ids = request.query_params.getlist('ids[]')

    links = MainHandler.get_ids_links([int(i) for i in ids])
    return HttpResponse(json.dumps(links), headers=HEADERS)

@api_view(['GET'])
# Short description of resources by ids
def get_short_descriptions(request):
    ids = request.query_params.getlist('ids[]')

    short_descriptions = MainHandler.get_ids_short_descriptions([int(i) for i in ids])
    return HttpResponse(json.dumps(short_descriptions), headers=HEADERS)

@api_view(['GET'])
def get_data(request):
    data = MainHandler.get_content(request.query_params)

    return HttpResponse(json.dumps({ 'borders': data }), headers=HEADERS)

@api_view(['GET'])
def get_content(request):
    content = MainHandler.get_content(request.query_params)

    return HttpResponse(json.dumps(content), headers=HEADERS)
