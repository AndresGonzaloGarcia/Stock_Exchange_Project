import django
import os
from yahoo_fin.stock_info import tickers_dow
from .website.models import TickerCode


# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_website.settings')
django.setup()


stock_df = tickers_dow(include_company_data= True)[['Company', 'Symbol']]
for idx, row in stock_df.iterrows():
    ticker_code = TickerCode(title= row['Company'], ticker= row['Symbol'])
    ticker_code.save()
    
print("Tabla creada y datos guardados exitosamente.")