
#CREATES DB OF ALL NASDAQ TICKERS

import django
import os
from yahoo_fin.stock_info import tickers_dow
from website.models import TickerCode


# Configures Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_website.settings')
django.setup()
