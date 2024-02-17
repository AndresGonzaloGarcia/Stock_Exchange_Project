from django.shortcuts import render
from website.models import Stocks
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_home(request, *arg, **kwargs):
    model_data = Stocks.objects.all()
    data = {}

    if model_data:
        data = model_to_dict(model_data)
        
    return Response(data)