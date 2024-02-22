from django.shortcuts import render, redirect
from yahoo_fin.stock_info import tickers_dow
from .models import TickerCode


def home(request):
    return render(request, 'home.html', {})

def stock_picker(request):
    if request.method == 'POST':
        stock_df = tickers_dow(include_company_data= True)[['Company', 'Symbol']]
        for idx, row in stock_df.iterrows():
            ticker_code = TickerCode(title= row['Company'], ticker= row['Symbol'])
            ticker_code.save()

    stock_ticker_list = TickerCode.objects.all()
    return render(request, 'stock_picker.html', {'stock_ticker_list': stock_ticker_list})

def stock_tracker(request):
    stock_picker = request.POST.getlist('selected_tickers')
    stocks_info = []
    
    return render(request, 'stock_tracker.html', {'stock_picker': stock_picker})

