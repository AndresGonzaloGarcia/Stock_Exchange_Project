from django.shortcuts import render
from yahoo_fin.stock_info import tickers_dow, get_live_price
from .models import TickerCode, Stocks


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
    Stocks.objects.all().delete() #elimino todos los datos previamente solicitados 
    
    for stock in stock_picker:
        stock_info = stock.split(',')
        stock_info.append(get_live_price(stock_info[1])) #uses the ticker of stocks info to access the live value 
        stock_values = Stocks(title= stock_info[0], ticker= stock_info[1], price= stock_info[2])
        stock_values.save()
        
    final_stocks_values = Stocks.objects.all()
    
    return render(request, 'stock_tracker.html', {'final_stocks_values': final_stocks_values})

