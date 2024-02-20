from django.shortcuts import render
from yahoo_fin.stock_info import tickers_dow

def home(request):
    return render(request, 'home.html', {})

def stock_picker(request):
    stock_list = tickers_dow()
    
    return render(request, 'stock_picker.html', {'stock_list': stock_list})

def stock_tracker(request):
    stock_picker = request.GET.getlist('stock_list')
    
    return render(request, 'stock_tracker.html', {})